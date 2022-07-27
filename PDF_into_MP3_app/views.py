import asyncio
from django.shortcuts import render
from .models import Note
import pytz
from datetime import datetime
from .func import createFileName
from .forms import newVoiceNoteForm
from django.core.files.storage import FileSystemStorage

def mainView(request):
    form = newVoiceNoteForm()
    if request.method == "GET":
        return render(request, "index.html",{'form':form})
    elif request.method == "POST":
        text = request.POST['text']
        pdf = request.POST['pdfFile']
        if pdf and text:
            return render(request, "index.html", {'form': form,
                                                  "error":"Неверный ввод данных: Введены сразу оба поля"})
        if not (pdf or text):
            return render(request, "index.html", {'form': form,
                                                  "error": "Неверный ввод данных: Ничего не введено"})

        newNote = Note(
            fileName=createFileName(),
            dateTime=pytz.UTC.localize(datetime.now()),
            text=text,
            pdfFile = pdf,
        )
        newNote.save()
        return render(request, 'index.html', {"form":form, 'note':newNote})




