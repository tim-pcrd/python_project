from email import message
from tkinter import *
from tkinter import messagebox
from classes.user import User
import settings

class Register_Page:
    def __init__(self, register = Tk()):
        self.register = register
        register.title("Registreren")
        register.geometry("550x400+400+200")

        self.register.configure(bg=settings.PROGRAM_BG)
        self.register.resizable(False, False)

        self.register.attributes('-topmost', True)

        self.email = Label(register, text="Email:", bg=settings.PROGRAM_BG)
        self.email.place(relx=0.100, rely=0.100, height=20, width=120)

        self.password = Label(register, text="Wachtwoord:", bg=settings.PROGRAM_BG)
        self.password.place(relx=0.100, rely=0.200, height=20, width=120)

        self.repeat_password = Label(register, text="Herhaal wachtwoord:", bg=settings.PROGRAM_BG)
        self.repeat_password.place(relx=0.100, rely=0.300, height=20, width=120)

        
        self.first_name = Label(register, text="Voornaam:", bg=settings.PROGRAM_BG)
        self.first_name.place(relx=0.100, rely=0.400, height=20, width=120)

        
        self.last_name = Label(register, text="Familienaam:", bg=settings.PROGRAM_BG)
        self.last_name.place(relx=0.100, rely=0.500, height=20, width=120)

        self.email_box = Entry(register)
        self.email_box.place(relx=0.440, rely=0.100, height=20, relwidth=0.35)

        self.password_box = Entry(register)
        self.password_box.place(relx=0.440, rely=0.200, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        self.repeat_password_box = Entry(register)
        self.repeat_password_box.place(relx=0.440, rely=0.300, height=20, relwidth=0.35)
        self.repeat_password_box.configure(show="*")
        self.repeat_password_box.configure(background="white")

        self.first_name_box = Entry(register)
        self.first_name_box.place(relx=0.440, rely=0.400, height=20, relwidth=0.35)

        self.last_name_box = Entry(register)
        self.last_name_box.place(relx=0.440, rely=0.500, height=20, relwidth=0.35)


        self.register_button = Button(register, text="Registreer", bg=settings.BUTTON_BG)
        self.register_button.place(relx=0.440, rely=0.600, height=30, relwidth=0.35)
        self.register_button.configure(command=self.register_user)

        self.message = None



    def register_user(self):
        email = self.email_box.get()
        password = self.password_box.get()
        repeat_password = self.repeat_password_box.get()
        first_name = self.first_name_box.get()
        last_name = self.last_name_box.get()

        
        if self.message:
            self.message.place_forget()

        # Controleer of alle velden zijn ingevuld
        if not email or not password or not repeat_password or not first_name or not last_name:
            self.error_message("*Niet alle velden zijn ingevuld")
            return

        # Controleer of wachtwoord minstens 4 tekens bevat
        if len(password) < 4:
            self.error_message('*Wachtwoord moet minstens 4 tekens bevatten')
            return

        #Controleer dat wachtwoord gelijk is aan herhaal wachtwoord
        if password != repeat_password:
            self.error_message("*Wachtwoorden komen niet overeen!")
            return


        # Controleer of email al bestaat in database
        if User.check_email_exists(email):
            self.error_message("*Dit emailadres is al in gebruik")
            return


        result = User.create_user(email, password, first_name, last_name)
        if result > 0:
            self.exit_register()
        else:
            self.error_message("Insert mislukt");
            return;

        
    def error_message(self, message):
        self.message = Label(self.register, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12))
        self.message.place(relx=0.100, rely=0.700, height=40, width=400)

    

    def exit_register(self):
        self.register.destroy()

    def mainloop_window(self):
        self.register.mainloop()