from tkinter import END, W, Button, Entry, Frame, Label, Listbox, OptionMenu
from classes.role import Role
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
        self.list_userIds = []
        for user in self.users:
            self.list_userIds.append(user.userID)
            self.users_list.insert(END, f'{user.first_name} {user.last_name}')


        self.list_btn = Button(self, text='Toon geselecteerde gebruiker', command=self.get_selected_user)
        self.list_btn.place(relx=0.05, rely=0.800, width=180)


        self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.first_name.place(relx=0.500, rely=0.100, height=20, width=120)

        self.first_name_box = Entry(self)
        self.first_name_box.place(relx=0.600, rely=0.100, height=20, width=150)

        self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.last_name.place(relx=0.500, rely=0.150, height=20, width=100)

        self.last_name_box = Entry(self)
        self.last_name_box.place(relx=0.600, rely=0.150, height=20, width=150)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.500, rely=0.200, height=20, width=120)

        self.email_box = Entry(self)
        self.email_box.place(relx=0.600, rely=0.200, height=20, width=150)

        self.role = Label(self, text="Rol:", bg=settings.PROGRAM_BG, anchor=W)
        self.role.place(relx=0.500, rely=0.25, height=20, width=120)

        self.roles = Role.get_all_roles()
        print(self.roles)
        # self.role_box = OptionMenu(self)


    
    def get_selected_user(self):

        self.clear_textboxes()

        selected_index = self.users_list.curselection()[0]
        print(self.list_userIds)
        print(selected_index)
        for x in self.users:
            if x.userID == self.list_userIds[selected_index]:
                self.selected_user = x
                print(self.selected_user)
                self.first_name_box.insert(0, f'{self.selected_user.first_name}')
                self.last_name_box.insert(0,f'{self.selected_user.last_name}')
                self.email_box.insert(0,f'{self.selected_user.email}')


    def clear_textboxes(self):
        self.first_name_box.delete("0",END)
        self.last_name_box.delete("0",END)
        self.email_box.delete("0",END)



        
 
