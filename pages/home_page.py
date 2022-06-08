from tkinter import Frame, Label
from classes.user import User
import settings


class Home_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        self.name_label = Label(self, text=f'Hallo {user.first_name}', bg=settings.PROGRAM_BG, font=("Arial", 13), fg='blue')
        self.name_label.place(x=5, y=10, height=20, width=120)
    