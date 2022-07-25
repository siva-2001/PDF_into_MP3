import asyncio
from django.shortcuts import render
from .models import Note
import pytz
from datetime import datetime
from .func import createFileName


def mainView(request):
    if request.method == "GET":
    #     return render(request, "index.html")
    # elif request.method == "POST":
    #     myText = "Я - самозванец, и меня наверняка разоблачат!"
    #     fileName = createFileName()
    #     newNote = Note(
    #         fileName = fileName,
    #         dateTime = pytz.UTC.localize(datetime.now()),
    #         text = myText,
    #     )
    #     newNote.save()
        return render(request, 'index.html')




