import os.path
from random import randint as rand
from PDF_into_MP3.settings import MEDIA_ROOT

def createFileName():
    namesFileAdd = open(os.path.join(MEDIA_ROOT, "namesFile.txt"), 'a+')
    namesFileRead = open(os.path.join(MEDIA_ROOT, "namesFile.txt"), 'r')
    names = namesFileRead.readlines()
    newName = 'MP3File_' + str(rand(10000, 99999)) + ".mp3\n"
    if(newName in names):
        while(newName in names):
            newName = 'MP3File_' + str(rand(1, 10)) + ".mp3\n"
    print(names)
    namesFileAdd.write(newName)
    return newName