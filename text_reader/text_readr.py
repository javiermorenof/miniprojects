import os
import pyttsx3
import PyPDF4
from configparser import ConfigParser
from config import *

#Creando función para la lectura de texto
def speech_starter(text, save=False, filename=False):
    
    #Opciones por defecto
    rate = 160
    voice = 'spanish'
    volume = 1    
    
    #Inicializando el motor de audio
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice)
    engine.setProperty('volume', volume)
    print(f"Opciones por defecto: Velocidad:{rate}, Idioma:{voice}, Volumen:{volume}")
    
    #Reproducción de audio
    engine.say(text)
    
    #Grabación de audio
    if save == True:
        engine.save_to_file(text, f'{filename}.mp3')
    else:
        pass
    engine.runAndWait()


#Creando un reader del texto en PDF
def text_reader(file, start_page=1, end_page=False):
    book = open(file, 'rb')
    reader = PyPDF4.PdfFileReader(book)
    numpages = reader.numPages
    print(f'Este documento tiene {numpages} páginas')
    text = ""
    if end_page == False:
        for k in range(start_page,numpages):
            page = reader.getPage(k)
            text_inpage = page.extractText()
            text += text_inpage
    else:
        for k in range(start_page,end_page):
            page = reader.getPage(k)
            text_inpage = page.extractText()
            text += text_inpage           
    return text

def text_cleaner(text):
    text = text.replace('-\n','')
    text = text.replace('\nŠ','')
    text = text.replace('\n',' ')
    return text

if __name__ == '__main__':

        try:
            save =  bool(save)
        except:
            print("No se ha indicado correctamente si se debe guardar o no el audio en formato mp3. Configura el archivo config.py indicando True or False en el campo 'Save'")
            
        try:
            start_page = int(start_page)
        except:
            print("Start_page no es un número en el documento 'config.py'.")
           
        try:
            end_page = bool(end_page)
        except:
            print("End_page no es True o False en el documento 'config.py'. Modifícalo a uno d eestos parámetros.")
            
       
        if origin_file not in os.listdir():
            print("El PDF no se encuentra en esta carpeta. Por favor, indica un documento válido existente")
        else:
            text = text_reader(origin_file, start_page, end_page)
            text = text_cleaner(text)
            speech_starter(text, save=save, filename=filename)  