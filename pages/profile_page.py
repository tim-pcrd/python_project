from tkinter import *

class Profile_Page:
    def __init__(self, root: Tk, width, height) -> None:

        self.frame = Frame(root)

        label = Label(self.frame, text="Profiel", relief=RAISED)
        label.pack()