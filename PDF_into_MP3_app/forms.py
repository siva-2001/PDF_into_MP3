from django import forms
from .models import Note

class newVoiceNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text', 'pdfFile']
        widgets = {
            "text":forms.widgets.Textarea(attrs={
                "id":"text_id",
                "type":"text",
                "class":"form-control",
                "placeholder":"Введите текст...",
                #"required":'',
                "style":"resize:none"
            }),
            "pdfFile":forms.widgets.FileInput(attrs={
                "id":"pdf_id",
                "class":"form-control",
                "placeholder": "Загрузите файл...",
                #"required": '',
            })
        }


