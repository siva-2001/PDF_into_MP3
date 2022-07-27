from django.db import models
from gtts import gTTS
from django.core.files import File
import pdftotext

class Note(models.Model):
    fileName = models.CharField(max_length=5)
    dateTime = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.CharField(max_length=10000, blank=True)
    pdfFile = models.FileField(upload_to="pdf/", blank=True)
    mp3File = models.FileField(upload_to="mp3/", blank=True)

    #async def save(self, *args, **kwargs):
    def save(self, *args, **kwargs):
        if self.text:
            f = open("temporaryFiles/MP3File.mp3", 'wb')
            gTTS(text=self.text, lang='ru').write_to_fp(f)
            f.close()
            f = open("temporaryFiles/MP3File.mp3", 'rb')
            self.mp3File.save(self.fileName, File(f), save=False)
            f.close()
        else:
            with open("temporaryFiles/tempFile.pdf", "rb") as f:
                pdfText = pdftotext.PDF(f)
                text = ''
                for string in pdfText:
                    text = text + string
                f = open("temporaryFiles/MP3File.mp3", 'wb')
                gTTS(text=text, lang='ru').write_to_fp(f)
                f.close()
                f = open("temporaryFiles/MP3File.mp3", 'rb')
                self.mp3File.save(self.fileName, File(f), save=False)
                f.close()
        super(Note, self).save(*args, **kwargs)
