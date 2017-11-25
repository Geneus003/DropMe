from tkinter import *
from PIL import Image, ImageDraw
from PIL import ImageTk
import os.path
from threading import Thread

from tkinter import *

root = Tk()
root.minsize(width=1280, height=720)

def registerScreen():

    DropMe_Logo = ImageTk.PhotoImage(file = "images/DropmeLogo.png")

    root["bg"] = "#1d1d1d"

    DropMe_Label = Label(root, image = DropMe_Logo, bg='#1d1d1d')
    Login_label = Label(root,text = "Login",font = "Serene 25",height = 1,width = 5,bg = '#1d1d1d',fg = "White")
    Password_label = Label(root, text = "Password",font = "Serene 25",height = 1,width = 8,bg = "#1d1d1d",fg = "White")
    Login_Entry = Entry(root,font = "Serene 25",width = 20, fg = "black",highlightthickness=0, relief='ridge',bd = 0)
    Register_Entry = Entry(root,font = "Serene 25",width = 20,fg = 'black',highlightthickness = 0,relief = "ridge",bd = 0)
    Entry_But = Button(root)

    DropMe_Label.image = DropMe_Logo


    DropMe_Label.place(x = 360, y = 10)
    Login_label.place(x = 400,y = 250)
    Password_label.place(x = 400,y = 380)
    Login_Entry.place(x = 410,y = 315)
    Register_Entry.place(x = 410, y = 445)


def DropMe():
    registerScreen()
    root.mainloop()

DropMe()

