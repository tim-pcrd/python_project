from tkinter import *

from numpy import RAISE

class Login(Frame):
    def __init__(self, root, width, height):
        super().__init__(root, width=width, height=height)

        self.configure(bg='blue')

        label = Label(self, text="login", relief=RAISED)
        label.pack()

        





    