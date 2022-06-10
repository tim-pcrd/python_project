from distutils.dep_util import newer_pairwise
from tkinter import ANCHOR, DISABLED, E, END, NORMAL, SOLID, W, Button, Entry, Frame, Label, Listbox, OptionMenu, StringVar
from tkinter.messagebox import askyesno, askyesnocancel
from tkinter.ttk import Combobox
from classes.role import Role
from classes.user import User
import settings

class Users_Admin_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)



        self.current_user = user
        
        self.message= None
        self.selected_user = None

        self.root = root

        self.selected_user_form_components = []

        self.configure(bg=settings.PROGRAM_BG)
        
        self.users_list_label = Label(self, text="Gebruikers:", bg=settings.PROGRAM_BG, anchor=W, font=("Arial", 12))
        self.users_list_label.place(x=20, rely=0.05, height=20, width=120)

        self.users_list = Listbox(self, exportselection=False)
        self.users_list.place(x=20, rely=0.100, height=350, width=180)
        self.users_list.bind('<<ListboxSelect>>', self.get_selected_user)

        self.new_user_btn = Button(self, text="Nieuwe gebruiker", command=self.show_new_user_frame, bg=settings.BUTTON_BG)
        self.new_user_btn.place(x=20, rely=0.700, width=180)
        

        self.fill_userslist()

        # self.list_btn = Button(self, text='Toon geselecteerde gebruiker', command=self.get_selected_user)
        # self.list_btn.place(relx=0.05, rely=0.800, width=180)


        self.selected_user_label = Label(self, text="Geselecteerde gebruiker:", bg=settings.PROGRAM_BG, anchor=W, font=("Arial", 12))
        self.selected_user_label.place(relx=0.230, rely=0.05, height=20, width=200)
        
        self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.first_name.place(relx=0.230, rely=0.100, height=20, width=120)
        

        self.first_name_box = Entry(self)
        self.first_name_box.place(relx=0.350, rely=0.100, height=20, width=180)
        self.selected_user_form_components.append(self.first_name_box)

        self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.last_name.place(relx=0.230, rely=0.150, height=20, width=100)
        

        self.last_name_box = Entry(self)
        self.last_name_box.place(relx=0.350, rely=0.150, height=20, width=180)
        self.selected_user_form_components.append(self.last_name_box)

        self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.email.place(relx=0.230, rely=0.200, height=20, width=120)

        self.email_box = Entry(self)
        self.email_box.place(relx=0.350, rely=0.200, height=20, width=180)
        self.selected_user_form_components.append(self.email_box)

        self.role = Label(self, text="Rol:", bg=settings.PROGRAM_BG, anchor=W)
        self.role.place(relx=0.230, rely=0.25, height=20, width=120)

        self.roles = Role.get_all_roles()
        
        self.role_combobox = Combobox(self, values=[x.role for x in self.roles])
        self.role_combobox.place(relx=0.350, rely=0.25, height=20, width=180)
        self.selected_user_form_components.append(self.role_combobox)


        self.save_btn = Button(self, text='Opslaan', command=self.save_selected_user, bg=settings.BUTTON_BG)
        self.save_btn.place(relx=0.350, rely=0.30, width=180)
        self.selected_user_form_components.append(self.save_btn)

        self.password = Label(self, text="Nieuw wachtwoord", bg=settings.PROGRAM_BG)
        self.password.place(relx=0.230, rely=0.40, height=20, width=120)

        self.repeat_password = Label(self, text="Herhaal wachtwoord", bg=settings.PROGRAM_BG)
        self.repeat_password.place(relx=0.230, rely=0.45, height=20, width=120)

        self.password_box = Entry(self)
        self.password_box.configure(show="*")
        self.password_box.place(relx=0.350, rely=0.40, height=20, width=180)
        self.selected_user_form_components.append(self.password_box)

        self.repeat_password_box = Entry(self)
        self.repeat_password_box.configure(show="*")
        self.repeat_password_box.place(relx=0.350, rely=0.45, height=20, width=180)
        self.selected_user_form_components.append(self.repeat_password_box)

        self.save_password_btn = Button(self, text='Wachtwoord wijzigen', command=self.change_password_selected_user, bg=settings.BUTTON_BG)
        self.save_password_btn.place(relx=0.350, rely=0.50, width=180)
        self.selected_user_form_components.append(self.save_password_btn)

        
        self.cancel_user_btn = Button(self, text='Annuleer', command=self.cancel_selected_user, bg=settings.WARNING_BUTTON_BG)
        self.cancel_user_btn.place(relx=0.350, rely=0.60, width=180)
        self.selected_user_form_components.append(self.cancel_user_btn)


        self.delete_user_btn = Button(self, text='Gebruiker verwijderen', command=self.delete_selected_user, bg=settings.DANGER_BUTTON_BG, fg=settings.DANGER_BUTTON_FG)
        self.delete_user_btn.place(relx=0.350, rely=0.65, width=180)
        self.selected_user_form_components.append(self.delete_user_btn)


        self.disable_form()



        # self.role_box = OptionMenu(self)


    def disable_form(self):
        for control in self.selected_user_form_components:
            control.configure(state=DISABLED)


    def enable_form(self):
        for control in self.selected_user_form_components:
            control.configure(state=NORMAL)

    
    def get_selected_user(self, event):
        self.clear_textboxes()
        self.clear_message()

        self.enable_form()

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


    def clear_selected_user(self):
        self.selected_user = None
        self.users_list.selection_clear(0,END)
        self.clear_textboxes()
        self.disable_form()


    def fill_userslist(self):
        self.users_list.delete(0,'end')
        self.users = self.current_user.select_all_users(self.current_user.userID)
        self.list_userIds = []
        for user in self.users:
            self.list_userIds.append(user.userID)
            self.users_list.insert(END, f'{user.first_name} {user.last_name}')


    def save_selected_user(self):
        if not self.selected_user: return

        self.selected_user.first_name = self.first_name_box.get()
        self.selected_user.last_name = self.last_name_box.get()
        self.selected_user.email = self.email_box.get()
        self.selected_user.roleId = self.roles[self.role_combobox.current()].roleID

        if not self.selected_user.first_name or not self.selected_user.last_name or not self.selected_user.email or not self.selected_user.roleId:
            self.error_message("Niet alle velden zijn ingevuld")
            return

        if User.check_email_exists(self.selected_user.email, self.selected_user.userID):
            self.error_message('Emailadres is al in gebruik')
            return

        result = self.selected_user.save_user()

        if result:
            self.success_message('Succesvol opgeslagen')
        else:
            self.error_message('Er is een probleem opgetreden')

        self.clear_selected_user()
        self.fill_userslist()


    def change_password_selected_user(self):
        if not self.selected_user: return

        self.clear_message()
        
        new_password = self.password_box.get()
        repeat_password = self.repeat_password_box.get()

        if not new_password or len(new_password) < 4:
            self.error_message('Wachtwoord moet minstens 4 tekens bevatten.')
            return

        if new_password != repeat_password:
            self.error_message('Wachtwoorden komen niet overeen.')
            return

        result = self.selected_user.change_password(new_password)

        if result:
            self.success_message('Wachtwoord succesvol gewijzigd')
        else:
            self.error_message('Er is een probleem opgetreden')

        self.clear_selected_user()
        self.fill_userslist()

    def cancel_selected_user(self):
        if not self.selected_user: return

        self.clear_selected_user()


    def delete_selected_user(self):
        if not self.selected_user: return

        answer = askyesnocancel('Verwijderen','Bent je zeker dat je deze gebruiker wil verwijderen?')
        if not answer: return

        result = self.selected_user.delete_user()

        if result:
            self.success_message('Gebruiker verwijderd')
        else:
            self.error_message('Er is een probleem opgetreden')

        self.clear_selected_user()
        self.fill_userslist()


    def clear_textboxes(self):
        self.first_name_box.delete("0",END)
        self.last_name_box.delete("0",END)
        self.email_box.delete("0",END)
        self.role_combobox.set('')
        self.password_box.delete("0",END)
        self.repeat_password_box.delete("0",END)


    def show_new_user_frame(self):

        self.clear_selected_user()

        self.new_user_frame = Frame(self, width=350, height=settings.HEIGHT, bg=settings.PROGRAM_BG)
        self.new_user_frame.place(relx=0.650, y=0, width=350, height=settings.HEIGHT)


        self.new_user_label = Label(self.new_user_frame, text="Nieuwe gebruiker:", bg=settings.PROGRAM_BG, anchor=W, font=("Arial", 12))
        self.new_user_label.place(x=10, rely=0.05, height=20, width=200)
        
        self.new_first_name = Label(self.new_user_frame, text="Voornaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.new_first_name.place(x=10, rely=0.100, height=20, width=120)

        self.new_first_name_box = Entry(self.new_user_frame)
        self.new_first_name_box.place(x=130, rely=0.100, height=20, width=180)

        self.new_last_name = Label(self.new_user_frame, text="Familienaam:", bg=settings.PROGRAM_BG,anchor=W)
        self.new_last_name.place(x=10, rely=0.150, height=20, width=100)

        self.new_last_name_box = Entry(self.new_user_frame)
        self.new_last_name_box.place(x=130, rely=0.150, height=20, width=180)

        self.new_email = Label(self.new_user_frame, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
        self.new_email.place(x=10, rely=0.200, height=20, width=120)

        self.new_email_box = Entry(self.new_user_frame)
        self.new_email_box.place(x=130, rely=0.200, height=20, width=180)

        self.new_role = Label(self.new_user_frame, text="Rol:", bg=settings.PROGRAM_BG, anchor=W)
        self.new_role.place(x=10, rely=0.25, height=20, width=120)

        self.new_role_combobox = Combobox(self.new_user_frame, values=[x.role for x in self.roles])
        self.new_role_combobox.place(x=130, rely=0.25, height=20, width=180)

        self.new_password = Label(self.new_user_frame, text="Nieuw wachtwoord", bg=settings.PROGRAM_BG,anchor=W)
        self.new_password.place(x=10, rely=0.30, height=20, width=120)

        self.new_repeat_password = Label(self.new_user_frame, text="Herhaal wachtwoord", bg=settings.PROGRAM_BG, anchor=W)
        self.new_repeat_password.place(x=10, rely=0.35, height=20, width=120)

        self.new_password_box = Entry(self.new_user_frame)
        self.new_password_box.configure(show="*")
        self.new_password_box.place(x=130, rely=0.30, height=20, width=180)

        self.new_repeat_password_box = Entry(self.new_user_frame)
        self.new_repeat_password_box.configure(show="*")
        self.new_repeat_password_box.place(x=130, rely=0.35, height=20, width=180)

        self.save_new_user_btn = Button(self.new_user_frame, text='Opslaan', command=self.save_new_user, bg=settings.BUTTON_BG)
        self.save_new_user_btn.place(x=130, rely=0.40, width=180)

        self.cancel_new_user_btn = Button(self.new_user_frame, text='Annuleer', command=self.cancel_new_user, bg=settings.WARNING_BUTTON_BG)
        self.cancel_new_user_btn.place(x=130, rely=0.45, width=180)



    def save_new_user(self):
        first_name = self.new_first_name_box.get()
        last_name = self.new_last_name_box.get()
        email = self.new_email_box.get()
        roleId = self.roles[self.new_role_combobox.current()].roleID
        new_password = self.new_password_box.get()
        new_repeat_password = self.new_repeat_password_box.get()

        if not first_name or not last_name or not email or not roleId or not new_password or not new_repeat_password:
            self.error_message("Niet alle velden zijn ingevuld")
            return

        if new_password != new_repeat_password:
            self.error_message("Wachtwoorden komen niet overeen")
            return

        if User.check_email_exists(email):
            self.error_message("*Dit emailadres is al in gebruik")
            return

        result = User.create_user(email, new_password, first_name, last_name, roleId)

        if result:
            self.success_message("Successvol opgeslagen")
        else:
            self.error_message("Er is een probleem opgetreden")

        self.fill_userslist()
        self.new_user_frame.destroy()
        self.clear_textboxes()


    def cancel_new_user(self):
        self.new_user_frame.destroy()


    def error_message(self, message):
        self.clear_message()
        self.message = Label(self, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12), anchor=W, padx=5, 
            highlightbackground="red", highlightcolor="red", highlightthickness=3)
        self.message.place(x=15, rely=0.910, height=40, width=400)
    
    def success_message(self, message):
        self.clear_message()
        self.message = Label(self, text=f"{message}", bg=settings.PROGRAM_BG, fg='green',font=("Arial", 12), anchor=W, padx=5,
            highlightbackground="green", highlightcolor="green", highlightthickness=3)
        self.message.place(x=15, rely=0.910, height=40, width=400)

    def clear_message(self):
        if self.message:
            self.message.destroy()



        
 
