from tkinter import Menu, Tk
from pages.home_page import Home_Page
from pages.login_page import *
from pages.register_page import Register_Page
from pages.users_admin_page import Users_Admin_Page
import settings
from classes.user import User
from pages.profile_page import Profile_Page
from pages.session_page import Session_Page
import settings

from pages.project_page import Project_Page
from pages.project_data_page import Project_Data_Page
from classes.project_session import ActiveSession
# from pages.session_page import Session_Page (klasse is nog niet gedefinieerd)
from pages.setup_page import Setup_Page



class Main_Win:

    def __init__(self,main_win = Tk()):

        self.user = None
        self.menubar = None
     
        self.main_win = main_win
        self.main_win.configure(bg=settings.PROGRAM_BG)
        self.main_win.resizable(False,False)
        main_win.title("Project")
        main_win.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

        self.open_login()


    def intialize_main(self):
        self.menubar = Menu(self.main_win)
        self.main_win.config(menu=self.menubar)
        self.menubar.add_command(
            label='Home',
            command=self.open_home
        )

        # User menu
        user_menu = Menu(self.menubar, tearoff=False)
        user_menu.add_command(
            label='Profiel',
            command=self.open_profile
        )

        # Controleer of user admin is
        if self.user.role == 'admin':
            user_menu.add_command(
                label='Admin',
                command=self.open_users_admin
            )

        user_menu.add_command(
            label='Uitloggen',
            command=self.open_logout
        )

        project_menu = Menu(self.menubar, tearoff=False)
        # session_menu = Menu(menubar, tearoff=False)


        #Session menu
        session_menu = Menu(self.menubar, tearoff=False)

        session_menu.add_command(
            label='Choose session+setup',
            command=self.open_session
        )

        #setup menu
        setup_menu = Menu(self.menubar, tearoff=False)

        project_menu.add_command(
            label='Project Manager',
            command=self.open_project
        )
        # session_menu.add_command(
        #     label='Session Manager',
        #     command=self.open_session
        # )
        setup_menu.add_command(
            label='Setup Manager',
            command=self.open_setup
        )


        self.menubar.add_cascade(label='Gebruiker', menu=user_menu)
        self.menubar.add_cascade(label='Project', menu=project_menu)
        # menubar.add_cascade(label='Session', menu=session_menu)
        self.menubar.add_cascade(label='Session', menu=session_menu)
        self.menubar.add_cascade(label='Setup', menu=setup_menu)

        self.open_home()

    def clear_menu(self):
        self.menubar.destroy()

    def open_login(self):
        self.destroy_all_pages()
        self.user = User()
        self.login_page = Login_Page(self.main_win, self, width=settings.WIDTH, height=settings.HEIGHT, user=self.user)
        self.login_page.place(x=0,y=0)

    def open_register(self):
        self.destroy_all_pages()
        self.register_page = Register_Page(self.main_win, self, width=settings.WIDTH, height=settings.HEIGHT)
        self.register_page.place(x=0,y=0)


    def mainloop_window(self): 
        self.main_win.mainloop()

    def open_logout(self):
        self.clear_menu()
        self.open_login()

    def open_home(self):
        self.destroy_all_pages()
        self.home_page = Home_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT, user=self.user)
        self.home_page.place(x=0, y=0)

    def open_profile(self):
        self.destroy_all_pages()
        self.profile_page = Profile_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT, user=self.user)    
        self.profile_page.place(x=0, y=0)

    def open_users_admin(self):
        self.destroy_all_pages()
        self.users_admin_page = Users_Admin_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT, user=self.user)
        self.users_admin_page.place(x=0, y=0)

    def open_project(self):
        self.destroy_all_pages()
        self.project_page = Project_Page(self.main_win, window_object_before_calling_mainloop, width=settings.WIDTH, height=settings.HEIGHT, user=self.user)
        self.project_page.place(x=0, y=0)

    def open_session(self):
        self.destroy_all_pages()
        self.session_page = Session_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT,user=self.user)
        self.session_page.place(x=0, y=0)

    # display the selected project's data
    def open_project_data(self, selected_project_id):
        self.destroy_all_pages()
        self.project_data_page = Project_Data_Page(self.main_win, selected_project_id, width=settings.WIDTH,
                                                   height=settings.HEIGHT, user=self.user)
        self.project_data_page.place(x=0, y=0)

    def open_setup(self):
        self.destroy_all_pages()
        self.setup_page = Setup_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT,user=self.user)
        self.setup_page.place(x=0, y=0)

    def destroy_all_pages(self):
        for page in self.main_win.place_slaves():
            page.destroy()

main_win = Main_Win()

print("Dit is main_win:", main_win)
window_object_before_calling_mainloop = main_win

main_win.mainloop_window()
