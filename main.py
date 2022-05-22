from tkinter import *
from tkinter import messagebox
from pages.login_page import *
from pages.profile_page import Profile_Page
from classes.user import User
import settings


user = User()

login_page = Login_Page(user) 
login_page.mainloop_window()

#Als user inlog scherm verlaat, programma stoppen
if not user.logged_in:
    exit()

class Main_Win:

    def __init__(self,main_win = Tk()):
     
        self.main_win = main_win
        self.main_win.configure(bg=settings.PROGRAM_BG)
        self.main_win.resizable(False,False)
        main_win.title("Project")
        main_win.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

        self.profile_page = Profile_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT,user=user)

        menubar = Menu(self.main_win)
        self.main_win.config(menu=menubar)

        # User menu
        user_menu = Menu(menubar, tearoff=False)
        user_menu.add_command(
            label='Profiel',
            command=self.open_profile
        )     
        user_menu.add_command(
            label='Uitloggen',
            command=self.open_logout
        )

        #Project menu
        project_menu = Menu(menubar, tearoff=False)

        setup_menu = Menu(menubar, tearoff=False)

        menubar.add_cascade(label='Gebruiker', menu=user_menu)
        menubar.add_cascade(label='Project', menu=project_menu)
        menubar.add_cascade(label='Setup', menu=setup_menu)


    def mainloop_window(self): 
        self.main_win.mainloop()

    def open_logout(self):
        self.unplace_all_pages()

    def open_profile(self):
        self.unplace_all_pages()
        self.profile_page.place(x=0,y=0)

    def unplace_all_pages(self):
        for page in self.main_win.place_slaves():
            page.place_forget()


main_win = Main_Win()

main_win.mainloop_window()


        
