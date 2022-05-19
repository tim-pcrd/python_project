from tkinter import *
from tkinter import messagebox
from classes.user import User
from PIL import ImageTk,Image  
import settings
import mysql.connector
from mysql.connector import (connection)

import mysql.connector
from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')
mycursor = db.cursor()

class Login_Page:

    def __init__(self,user: User,login = Tk()):
    
        self.login = login
        login.title("Login")
        login.geometry("550x230+400+200")
        self.logged_in = False
        self.user = user

        self.login.configure(bg=settings.PROGRAM_BG)
        self.login.resizable(False, False)


        self.image_canvas = Canvas(login, width=80, height=80)
        self.image_canvas.place(x=0, y=0) 
        self.img = ImageTk.PhotoImage(Image.open("images/muziek.jpg"))  
        self.image_canvas.create_image(1, 1, anchor=NW, image=self.img) 

        self.username = Label(login, text="Gebruikersnaam:", bg=settings.PROGRAM_BG)
        self.username.place(relx=0.150, rely=0.298, height=20, width=120)

        self.password = Label(login, text="Wachtwoord:", bg=settings.PROGRAM_BG)
        self.password.place(relx=0.150, rely=0.468, height=20, width=120)


        self.login_button = Button(login, text="Login", bg=settings.BUTTON_BG)
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit", bg=settings.BUTTON_BG)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)


        self.username_box = Entry(login)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

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

    def cb(self, ):

        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

    def login_user(self):
        name = self.username_box.get()
        password = self.password_box.get()
        login_completed = self.login_completed.get()

        #database call komt hier

        db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                 host='35.157.16.43',
                                 database='sql11491613')

        mycursor = db.cursor()
        db_name= "sql11491613"

        users=mycursor.execute(f"SELECT * FROM users where password='{password}' and firstName='{name}';")
        for user in mycursor:
            self.user.userID = user[0]
            self.user.roleId = user[1]
            self.user.last_name = user[2]
            self.user.first_name = user[3]
            self.user.email = user[4]
            self.user.stage_name = user[6]
            self.user.manager = user[7]

        if self.user.userID:
            self.user.logged_in = True
            self.login.destroy() 
            self.login_completed == 1

        else:
            messagebox.showwarning("Gebruikersnaam of wachtwoord verkeerd!")


    def exit_login(self):
        msg = messagebox.askyesno("Exit login", "Wil je login verlaten?")
        if (msg):
            exit()

    def mainloop_window(self):
        self.login.mainloop()