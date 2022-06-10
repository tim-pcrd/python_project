from email import message
from tkinter import *
from tkinter import messagebox
from classes.helper import Helper
from classes.user import User
import settings

class Register_Page(Frame):

    def __init__(self, root, main_win, width, height):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        self.main_win = main_win


        self.title = Label(self, text="Registreren", bg=settings.PROGRAM_BG,font=("Arial", 16), fg='blue', anchor=W)
        self.title.place(x=10, y=10, height=40, width=130)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.250, rely=0.200, height=20, width=120)

        self.password = Label(self, text="Wachtwoord:", bg=settings.PROGRAM_BG, anchor=W)
        self.password.place(relx=0.250, rely=0.300, height=20, width=120)

        self.repeat_password = Label(self, text="Herhaal wachtwoord:", bg=settings.PROGRAM_BG, anchor=W)
        self.repeat_password.place(relx=0.250, rely=0.400, height=20, width=120)

        
        self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG, anchor=W)
        self.first_name.place(relx=0.250, rely=0.500, height=20, width=120)

        
        self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG, anchor=W)
        self.last_name.place(relx=0.250, rely=0.600, height=20, width=120)

        self.email_box = Entry(self)
        self.email_box.place(relx=0.440, rely=0.200, height=20, relwidth=0.30)

        self.password_box = Entry(self)
        self.password_box.place(relx=0.440, rely=0.300, height=20, relwidth=0.30)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        self.repeat_password_box = Entry(self)
        self.repeat_password_box.place(relx=0.440, rely=0.400, height=20, relwidth=0.30)
        self.repeat_password_box.configure(show="*")
        self.repeat_password_box.configure(background="white")

        self.first_name_box = Entry(self)
        self.first_name_box.place(relx=0.440, rely=0.500, height=20, relwidth=0.30)

        self.last_name_box = Entry(self)
        self.last_name_box.place(relx=0.440, rely=0.600, height=20, relwidth=0.30)


        self.register_button = Button(self, text="Registreer", bg=settings.BUTTON_BG)
        self.register_button.place(relx=0.440, rely=0.700, height=30, relwidth=0.30)
        self.register_button.configure(command=self.register_user)


        self.to_login_button = Button(self, text="Login", bg=settings.BUTTON_BG)
        self.to_login_button.place(relx=0.83, y=20, height=30, relwidth=0.15)
        self.to_login_button.configure(command=self.to_login)

        self.message = None



    def register_user(self):
        email = self.email_box.get()
        password = self.password_box.get()
        repeat_password = self.repeat_password_box.get()
        first_name = self.first_name_box.get()
        last_name = self.last_name_box.get()

        Helper.clear_message(self)

        # Controleer of alle velden zijn ingevuld
        if not email or not password or not repeat_password or not first_name or not last_name:
            Helper.error_message(self, "*Niet alle velden zijn ingevuld")
            return

        # Controleer of wachtwoord minstens 4 tekens bevat
        if len(password) < 4:
            Helper.error_message(self, '*Wachtwoord moet minstens 4 tekens bevatten')
            return

        #Controleer dat wachtwoord gelijk is aan herhaal wachtwoord
        if password != repeat_password:
            Helper.error_message(self, "*Wachtwoorden komen niet overeen!")
            return


        # Controleer of email al bestaat in database
        if User.check_email_exists(email):
            Helper.error_message(self, "*Dit emailadres is al in gebruik")
            return


        result = User.create_user(email, password, first_name, last_name)
        if result > 0:
            Helper.success_message(self, 'Succesvol geregistreerd')
            return
        else:
            Helper.error_message(self, "Insert mislukt");
            return;


    def to_login(self):
        self.main_win.open_login()

        

    
