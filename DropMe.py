from tkinter import *
from PIL import Image, ImageDraw
from PIL import ImageTk
import os.path
from threading import Thread

from tkinter import *

root = Tk()
root.minsize(width=1280, height=720)

def registerScreen():

    root["bg"] = "#5D9CE5"

    DropMe_Label= Label(root, text="DropMe", font="Arial 60", height=1, width=6, bd=0, bg='#5D9CE5', fg="white")
    Login_label = Label(root,text = "Login",font = "Arial 25",height = 1,width = 5,bg = '#5D9CE5',fg = "White")
    Password_label = Label(root, text = "Password",font = "Arial 25",height = 1,width = 8,bg = "#5D9CE5",fg = "White")
    Login_Entry = Entry(root,font = "Arial 25",width = 20,bg = "#5D9CE5", fg = "white",highlightthickness=0, relief='ridge',bd = 0)

    DropMe_Label.place(x = 500, y = 50)
    Login_label.place(x = 400,y = 250)
    Password_label.place(x = 400,y = 380)
    Login_Entry.place(x = 410,y = 315)


def DropMe():
    registerScreen()
    root.mainloop()

DropMe()

