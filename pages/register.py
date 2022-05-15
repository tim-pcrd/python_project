from tkinter import *

class Register(Frame):
    def __init__(self, root, width, height):
        super().__init__(root, width=width, height=height)

        label = Label(self, text="register", relief=RAISED)
        label.pack()