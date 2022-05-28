from tkinter import *
from tkinter import messagebox
from classes.user import User
# from PIL import ImageTk,Image

import settings

class Login_Page:

    def __init__(self,user: User,login = Tk()):
    
        self.login = login
        login.title("Login")
        login.geometry("550x230+400+200")
        self.user = user

        self.login.configure(bg=settings.PROGRAM_BG)
        self.login.resizable(False, False)


        # self.image_canvas = Canvas(login, width=80, height=80)
        # self.image_canvas.place(x=0, y=0) 
        # self.img = ImageTk.PhotoImage(Image.open("images/muziek.jpg"))  
        # self.image_canvas.create_image(1, 1, anchor=NW, image=self.img) 



        #login form

        self.email = Label(login, text="Email:", bg=settings.PROGRAM_BG)
        self.email.place(relx=0.150, rely=0.298, height=20, width=120)

        self.password = Label(login, text="Wachtwoord:", bg=settings.PROGRAM_BG)
        self.password.place(relx=0.150, rely=0.468, height=20, width=120)


        self.login_button = Button(login, text="Login", bg=settings.BUTTON_BG)
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit", bg=settings.BUTTON_BG)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)


        self.email_box = Entry(login)
        self.email_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = Entry(login)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")


        self.var = IntVar()
        self.show_password = Checkbutton(login)
        self.show_password.place(relx=0.150, rely=0.650, relheight=0.100, relwidth=0.250)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Toon wachtwoord''',bg=settings.PROGRAM_BG)
        self.show_password.configure(variable=self.var, command=self.cb)


        self.register_button = Button(login, text="Registeren", bg=settings.BUTTON_BG)
        self.register_button.place(relx=0.85, rely=0.05, height=30, width=70)
        self.register_button.configure(command=self.open_register)

        self.message= None

        
    def open_register(self):
        from pages.register_page import Register_Page
        self.register_win = Register_Page()
        self.register_win.mainloop_window()

    def cb(self, ):

        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

    def login_user(self):
        email= self.email_box.get()
        password = self.password_box.get()

        self.user.login_user(email, password)

        if self.user.userID:
            self.user.logged_in = True
            self.login.destroy()
            if self.message:
                self.message.place_forget()
        else:
            self.error_message('Wachtwoord of email niet correct')

    def error_message(self, message):
        self.message = Label(self.login, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12))
        self.message.place(relx=0.100, rely=0.800, height=40, width=400)


    def exit_login(self):
        msg = messagebox.askyesno("Exit login", "Wil je login verlaten?")
        if (msg):
            exit()

    def mainloop_window(self):
        self.login.mainloop()