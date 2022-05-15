from tkinter import *
from pages.login import Login
from pages.register import Register
import settings

class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
        self.login_page = Login(self, width=settings.WIDTH, height=settings.HEIGHT)
        self.register_page = Register(self, width=settings.WIDTH, height=settings.HEIGHT)

        menubar = Menu(self)
        self.config(menu=menubar)

        # User menu
        user_menu = Menu(menubar, tearoff=False)

        user_menu.add_command(
            label='Inloggen',
            command=self.open_login
        )
        
        user_menu.add_command(
            label='Uitloggen',
            command=self.open_logout
        )

        user_menu.add_command(
            label='Registreren',
            command=self.open_register
        )

        menubar.add_cascade(label='Gebruiker', menu=user_menu)

       
    def open_login(self):
        self.unplace_all_pages()
        self.login_page.place(x=0,y=0)

    def open_logout(self):
        self.unplace_all_pages()

    def open_register(self):
        self.unplace_all_pages()
        self.register_page.place(x=0,y=0)

    def unplace_all_pages(self):
        for page in self.place_slaves():
            page.place_forget()
        


app = App()

app.mainloop()