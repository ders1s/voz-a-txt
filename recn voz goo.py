

#grafico el inter es name clas
from tkinter import *
exter=Tk()
exter.title("Asistente voz a texto")

exter.iconbitmap("snorlax.ico")

#inter.geometry("650x450")
exter.config(bg="black")
exter.config(bd=45)
exter.config(relief="groove")


#frema interno ventana
rFrame=Frame()
#Frame estilo y color 
#rFrame.config(bg="chartreuse3")
rFrame.config(width="1000",height="650")
rFrame.config(bd=35)
rFrame.config(relief="sunken")
rFrame.config(cursor="hand2")

rFrame.pack()
Imagen=PhotoImage(file="asis.gif")
Label(rFrame, image=Imagen).place(x=300, y=0)
Label=Label(rFrame,text="Hola soy tu asistente personal dime algo para traducirlo a texto",font=("Comic Sans MS",22))
Label.place(x=30, y=300)

#fin interfz

import speech_recognition as sr 

r = sr.Recognizer()
#llamdo micro

with sr.Microphone() as source:
    print("Hola soy tu asistente personal dime algo para traducirlo a texto")
    audio = r.listen(source)
#usando recognize de google y estableciendo lenguaje español
    try:
        text = r.recognize_google(audio, language = 'es-Es')
        print("Repite porfavor:{}".format(text))
    except:
            print("Lo siento pero no puedo escucharte!")
           
exter.mainloop()
            