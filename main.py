import pages.login_page
from pages.users_admin_page import Users_Admin_Page
import settings
from classes.user import User
from pages.login_page import *
from pages.profile_page import Profile_Page
import settings

from pages.setup_page import Setup_Page

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

        menubar = Menu(self.main_win)
        self.main_win.config(menu=menubar)

        # User menu
        user_menu = Menu(menubar, tearoff=False)
        user_menu.add_command(
            label='Profiel',
            command=self.open_profile
        )

        # Controleer of user admin is
        if user.role == 'admin':
            user_menu.add_command(
                label='Admin',
                command=self.open_users_admin
            )

        user_menu.add_command(
            label='Uitloggen',
            command=self.open_logout
        )

        #Project menu
        project_menu = Menu(menubar, tearoff=False)

        setup_menu = Menu(menubar, tearoff=False)

        setup_menu.add_command(
            label='Setup Manager',
            command=self.open_setup
        )




        menubar.add_cascade(label='Gebruiker', menu=user_menu)
        menubar.add_cascade(label='Project', menu=project_menu)
        menubar.add_cascade(label='Setup', menu=setup_menu)


    def mainloop_window(self): 
        self.main_win.mainloop()

    def open_logout(self):
        self.destroy_all_pages()
        exit()

    def open_profile(self):
        self.destroy_all_pages()
        self.profile_page = Profile_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT, user=user)    
        self.profile_page.place(x=0, y=0)

    def open_users_admin(self):
        self.destroy_all_pages()
        self.users_admin_page = Users_Admin_Page(self.main_win, width= settings.WIDTH, height=settings.HEIGHT, user=user)
        self.users_admin_page.place(x=0, y=0)

        

    def destroy_all_pages(self):
        for page in self.main_win.place_slaves():
            page.destroy()

    def open_setup(self):
        self.destroy_all_pages()
        self.setup_page = Setup_Page(self.main_win, width=settings.WIDTH, height=settings.HEIGHT,user=user)
        self.setup_page.place(x=0, y=0)



main_win = Main_Win()

main_win.mainloop_window()


        
