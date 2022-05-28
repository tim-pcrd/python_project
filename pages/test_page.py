from tkinter import Frame, Label
import settings


class Test(Frame):
    def __init__(self, root, width, height):
        super().__init__(root, width=width, height=height)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG)
        self.email.place(relx=0.150, rely=0.298, height=20, width=120)