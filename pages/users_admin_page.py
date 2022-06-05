from tkinter import END, W, Button, Entry, Frame, Label, Listbox, OptionMenu, StringVar
from tkinter.ttk import Combobox
from classes.role import Role
from classes.user import User
import settings

class Users_Admin_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.current_user = user

        self.configure(bg=settings.PROGRAM_BG)
        
        self.users_list_label = Label(self, text="Gebruikers:", bg=settings.PROGRAM_BG, anchor=W, font=("Arial", 12))
        self.users_list_label.place(relx=0.05, rely=0.05, height=20, width=120)

        self.users_list = Listbox(self, exportselection=False)
        self.users_list.place(relx=0.05, rely=0.100, height=300, width=180)
        self.users_list.bind('<<ListboxSelect>>', self.get_selected_user)

        self.fill_userslist()

        # self.list_btn = Button(self, text='Toon geselecteerde gebruiker', command=self.get_selected_user)
        # self.list_btn.place(relx=0.05, rely=0.800, width=180)


        
        self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.first_name.place(relx=0.500, rely=0.100, height=20, width=120)

        self.first_name_box = Entry(self)
        self.first_name_box.place(relx=0.600, rely=0.100, height=20, width=180)

        self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.last_name.place(relx=0.500, rely=0.150, height=20, width=100)

        self.last_name_box = Entry(self)
        self.last_name_box.place(relx=0.600, rely=0.150, height=20, width=180)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.500, rely=0.200, height=20, width=120)

        self.email_box = Entry(self)
        self.email_box.place(relx=0.600, rely=0.200, height=20, width=180)

        self.role = Label(self, text="Rol:", bg=settings.PROGRAM_BG, anchor=W)
        self.role.place(relx=0.500, rely=0.25, height=20, width=120)

        self.roles = Role.get_all_roles()
        
        self.role_combobox = Combobox(self, values=[x.role for x in self.roles])
        self.role_combobox.place(relx=0.600, rely=0.25, height=20, width=180)


        self.save_btn = Button(self, text='Opslaan', command=self.save_selected_user)
        self.save_btn.place(relx=0.600, rely=0.30, width=180)

        self.message= None
        self.selected_user = None


        # self.role_box = OptionMenu(self)


    
    def get_selected_user(self, event):
        print(event)
        self.clear_textboxes()

        selected_index = self.users_list.curselection()[0]
        for x in self.users:
            if x.userID == self.list_userIds[selected_index]:
                self.selected_user = x
                print(self.selected_user)
                self.first_name_box.insert(0, f'{self.selected_user.first_name}')
                self.last_name_box.insert(0,f'{self.selected_user.last_name}')
                self.email_box.insert(0,f'{self.selected_user.email}')
                self.role_combobox.set(f'{self.selected_user.role}');
                print(self.role_combobox.current())


    def save_selected_user(self):
        if not self.selected_user: return

        self.selected_user.first_name = self.first_name_box.get()
        self.selected_user.last_name = self.last_name_box.get()
        self.selected_user.email = self.email_box.get()
        self.selected_user.roleId = self.roles[self.role_combobox.current()].roleID

        result = self.selected_user.save_user()

        if result:
            self.success_message('Succesvol opgeslagen')
        else:
            self.error_message('Er is een probleem opgetreden')

        self.clear_selected_user()
        self.fill_userslist()


    def clear_selected_user(self):
        self.selected_user = None
        self.clear_textboxes()


    def fill_userslist(self):
        self.users_list.delete(0,'end')
        self.users = self.current_user.select_all_users(self.current_user.userID)
        self.list_userIds = []
        for user in self.users:
            self.list_userIds.append(user.userID)
            self.users_list.insert(END, f'{user.first_name} {user.last_name}')
        

    def clear_textboxes(self):
        self.first_name_box.delete("0",END)
        self.last_name_box.delete("0",END)
        self.email_box.delete("0",END)
        self.role_combobox.set('')


    def error_message(self, message):
        self.clear_message()
        self.message = Label(self, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12))
        self.message.place(x=0, rely=0.920, height=40, width=400)
    
    def success_message(self, message):
        self.clear_message()
        self.message = Label(self, text=f"{message}", bg=settings.PROGRAM_BG, fg='green',font=("Arial", 12))
        self.message.place(x=0, rely=0.920, height=40, width=400)

    def clear_message(self):
        if self.message:
            self.message.destroy()



        
 
