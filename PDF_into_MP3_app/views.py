import asyncio
from django.shortcuts import render
from .models import Note
import pytz
from datetime import datetime
from .func import createFileName
from .forms import newVoiceNoteForm
from django.core.files.storage import FileSystemStorage
import pdftotext
from django.utils.datastructures import MultiValueDictKeyError

def mainView(request):
    form = newVoiceNoteForm()
    if request.method == "GET":
        data = {"form":form}
    elif request.method == "POST":
        text = request.POST.get('text', False)
        pdf = request.FILES.get('pdfFile', False)
        if pdf and text:
            data = {'form': form, "error":"Неверный ввод данных: Введены сразу оба поля"}
        elif (not (pdf or text)):
            data = {'form': form, "error": "Неверный ввод данных: Ничего не введено"}
        else:
            newNote = Note(
                fileName=createFileName(),
                dateTime=pytz.UTC.localize(datetime.now()),
                text=text,
                pdfFile = pdf,
            )
            if pdf:
                with open("temporaryFiles/tempFile.pdf", "wb") as f:
                    for string in pdf:
                        f.write(string)
            newNote.save()
            data = {"form":form, 'note':newNote}
    return render(request, 'index.html', data)




