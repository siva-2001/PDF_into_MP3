from django.db import models

class Note(models.Model):
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.CharField(max_length=10000)
    mp3File = models.FileField(upload_to="mp3")
