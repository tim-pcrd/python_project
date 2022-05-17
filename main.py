from tkinter import *
from tkinter import messagebox
from pages.login_page import *
import settings


login_page = Login_Page() 
login_page.mainloop_window()


class Main_Win:

    def __init__(self,main_win = Tk()):
     
        self.main_win = main_win
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
        
        user_menu.add_command(
            label='Uitloggen',
            command=self.open_logout
        )

        #         self.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
#         self.login_page = Login(self, width=settings.WIDTH, height=settings.HEIGHT)
#         self.register_page = Register(self, width=settings.WIDTH, height=settings.HEIGHT)

        menubar.add_cascade(label='Gebruiker', menu=user_menu)


    def mainloop_window(self): 
        self.main_win.mainloop()

    def open_logout(self):
        self.unplace_all_pages()

    def open_profile(self):
        self.unplace_all_pages()
        # self.register_page.place(x=0,y=0)

    def unplace_all_pages(self):
        for page in self.main_win.place_slaves():
            page.place_forget()


main_win = Main_Win()

main_win.mainloop_window()


# class App(Tk):
#     def __init__(self):
#         super().__init__()

#         self.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
#         self.login_page = Login(self, width=settings.WIDTH, height=settings.HEIGHT)
#         self.register_page = Register(self, width=settings.WIDTH, height=settings.HEIGHT)

#         menubar = Menu(self)
#         self.config(menu=menubar)

#         # User menu
#         user_menu = Menu(menubar, tearoff=False)

#         user_menu.add_command(
#             label='Inloggen',
#             command=self.open_login
#         )
        
#         user_menu.add_command(
#             label='Uitloggen',
#             command=self.open_logout
#         )

#         user_menu.add_command(
#             label='Registreren',
#             command=self.open_register
#         )

#         menubar.add_cascade(label='Gebruiker', menu=user_menu)

       
#     def open_login(self):
#         self.unplace_all_pages()
#         self.login_page.place(x=0,y=0)

#     def open_logout(self):
#         self.unplace_all_pages()

#     def open_register(self):
#         self.unplace_all_pages()
#         self.register_page.place(x=0,y=0)

#     def unplace_all_pages(self):
#         for page in self.place_slaves():
#             page.place_forget()
        
