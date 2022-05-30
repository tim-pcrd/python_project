from tkinter import W, Button, Frame, Label, Listbox
from classes.user import User
import settings

class Users_Admin_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)
        
        self.users_list_label = Label(self, text="Gebruikers:", bg=settings.PROGRAM_BG, anchor=W, font=("Arial", 12))
        self.users_list_label.place(relx=0.05, rely=0.05, height=20, width=120)

        self.users_list = Listbox(self)
        self.users_list.place(relx=0.05, rely=0.100, height=300, width=180)

        self.users = user.select_all_users(user.userID)
        for user in self.users:
            self.users_list.insert(user.userID, f'{user.first_name} {user.last_name}')


        self.list_btn = Button(self, text='Toon geselecteerde gebruiker', command=self.get_selected_user)
        self.list_btn.place(relx=0.05, rely=0.800, width=180)


        self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.first_name.place(relx=0.500, rely=0.100, height=20, width=120)

        self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.last_name.place(relx=0.500, rely=0.150, height=20, width=120)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.500, rely=0.200, height=20, width=120)

        self.role = Label(self, text="Rol:", bg=settings.PROGRAM_BG, anchor=W)
        self.role.place(relx=0.500, rely=0.25, height=20, width=120)

    
    def get_selected_user(self):
        pass

        
 
