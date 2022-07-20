from django.shortcuts import render
from gtts import gTTS

def mainView(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        text = request.POST["text"]
        mp3_file = gTTS(text=text, lang="ru")
        mp3_file.save(f'file.mp3')
