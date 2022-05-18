from tkinter import *
import settings

class Profile_Page(Frame):
     def __init__(self, root, width, height):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        label = Label(self, text="profile", relief=RAISED)
        label.pack()

