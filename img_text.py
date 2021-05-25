#coding:utf-8
import os
import pytesseract
from PIL import Image
image_name = input("Exécuter ce script dans le meme dossier que l'image pour ne pas avoir à trop gérer des problèmes de chemin\nLe nom de l'image: ")
img=Image.open(image_name)
text=pytesseract.image_to_string(img)
print(text)
command='echo "{}" >> {}.txt'.format(text,image_name.split(".")[0]) 
os.system(command)
