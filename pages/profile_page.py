from tkinter import *
from classes.user import User
import settings

class Profile_Page(Frame):
     def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        label = Label(self, text=f'Hallo {user.first_name}', relief=RAISED)
        label.pack()

