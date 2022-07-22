from django.db import models
import os.path
from django.shortcuts import render
from gtts import gTTS
import tempfile
from django.core.files import File
import pytz
from datetime import datetime
from PDF_into_MP3.settings import MEDIA_ROOT
from .func import createFileName
from io import BytesIO

class Note(models.Model):
    fileName = models.CharField(max_length=5)
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.CharField(max_length=10000)
    mp3File = models.FileField(upload_to="mp3/", blank=True)

    def save(self, *args, **kwargs):
        f = open("file.mp3", 'wb')
        gTTS(text=self.text, lang='ru').write_to_fp(f)
        f.close()
        f = open("file.mp3", 'rb')
        self.mp3File.save(self.fileName+'.mp3', File(f), save=False)
        f.close()
        super(Note, self).save(*args, **kwargs)
