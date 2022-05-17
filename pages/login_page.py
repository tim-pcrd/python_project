from tkinter import *
from tkinter import messagebox

class Login_Page:

    def __init__(self,login = Tk()):
    
        self.login = login
        login.title("Login")
        login.geometry("450x230")


        self.username = Label(login, text="Gebruikersnaam:")
        self.username.place(relx=0.150, rely=0.298, height=20, width=120)

        self.password = Label(login, text="Wachtwoord:")
        self.password.place(relx=0.150, rely=0.468, height=20, width=120)


        self.login_button = Button(login, text="Login")
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit")
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
        self.show_password.place(relx=0.285, rely=0.650, relheight=0.100, relwidth=0.125)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Show''')
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

        if name == "user" and password == "1234":
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