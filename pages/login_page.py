from tkinter import *
from tkinter import messagebox
from classes.helper import Helper
from classes.user import User
# from PIL import ImageTk,Image

import settings

class Login_Page(Frame):
    def __init__(self, root, main_win, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        self.main_win = main_win
        self.user = user

        self.title = Label(self, text="Inloggen", bg=settings.PROGRAM_BG,font=("Arial", 16), fg='blue', anchor=W)
        self.title.place(x=10, y=10, height=40, width=130)


        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.250, rely=0.300, height=20, width=120)

        self.password = Label(self, text="Wachtwoord:", bg=settings.PROGRAM_BG, anchor=W)
        self.password.place(relx=0.250, rely=0.400, height=20, width=120)


      

        self.login_completed = IntVar()

        self.email_box = Entry(self)
        self.email_box.place(relx=0.440, rely=0.300, height=20, relwidth=0.30)

        self.password_box = Entry(self)
        self.password_box.place(relx=0.440, rely=0.400, height=20, relwidth=0.30)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")


        self.var = IntVar()
        self.show_password = Checkbutton(self, anchor=W)
        self.show_password.place(relx=0.25, rely=0.480, relheight=0.100, relwidth=0.200)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Toon wachtwoord''',bg=settings.PROGRAM_BG)
        self.show_password.configure(variable=self.var, command=self.cb)


        self.login_button = Button(self, text="Login", bg=settings.BUTTON_BG)
        self.login_button.place(relx=0.440, rely=0.500, height=30, relwidth=0.30)
        self.login_button.configure(command=self.login_user)


        self.register_button = Button(self, text="Registreren", bg=settings.BUTTON_BG)
        self.register_button.place(relx=0.83, y=20, height=30, relwidth=0.15)
        self.register_button.configure(command=self.open_register)


        self.message= None

        
    def open_register(self):
        self.main_win.open_register()

    def cb(self, ):

        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

    def login_user(self):
        email= self.email_box.get()
        password = self.password_box.get()

        if not email or not password:
            Helper.error_message(self, 'Niet alle velden zijn ingevuld')
            return

        self.user.login_user(email, password)

        if self.user.userID:
            self.user.logged_in = True
            if self.message:
                self.message.place_forget()
            self.main_win.intialize_main()
            
        else:
            Helper.error_message(self, 'Wachtwoord of email niet correct')
