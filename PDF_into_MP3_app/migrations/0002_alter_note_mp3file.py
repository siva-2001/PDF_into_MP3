# Generated by Django 4.0.6 on 2022-07-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PDF_into_MP3_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='mp3File',
            field=models.FileField(blank=True, upload_to='mp3/'),
        ),
    ]