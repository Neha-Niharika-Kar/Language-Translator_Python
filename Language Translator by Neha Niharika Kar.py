# import modules
from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
from gtts import gTTS
import os

# create window
root = Tk()
root.geometry('1080x400')
root.config(bg="black")
root.title("Language Translator")

# app icon
icon = PhotoImage(file="translate.png")
root.iconphoto(False,icon)

# list of languages
languages = googletrans.LANGUAGES
language = list(languages.values())
lang1 = languages.keys()

# input language widgets
source = ttk.Combobox(root, values=language, font="Cambria", width=30, state='r')
source.place(x=30,y=60)
source.set('English')

f1 = Frame(root, bg="red", bd=5)
f1.place(x=30, y=100, width=410, height=210)

text1 = Text(f1, font="Calibri", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=400, height=200)

# output language widgets
destin = ttk.Combobox(root, values=language, font="Cambria", width=30, state='r')
destin.place(x=760,y=60)
destin.set('Select Output Language')

f2 = Frame(root, bg="red", bd=5)
f2.place(x=642, y=100, width=410, height=210)

text2 = Text(f2, font="Calibri", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=400, height=200)

# translate function
def Translate():
    translator = Translator()
    translated = translator.translate(text= text1.get(1.0, END), source=source.get, dest = destin.get())
    text2.delete(1.0, END)
    text2.insert(END, translated.text)

# translate button
trans = Button(root, text="Translate", font="Cambria", activebackground="pink", cursor="hand2", bd=5, bg='blue', fg="white", command=Translate)
trans.place(x=500, y=200)

# execute program
root.mainloop()
