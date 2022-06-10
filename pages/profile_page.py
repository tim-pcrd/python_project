from email import message
from tkinter import *
from classes.db import Db
from classes.helper import Helper
from classes.user import User
import settings

class Profile_Page(Frame):
   def __init__(self, root, width, height, user: User):
      super().__init__(root, width=width, height=height)

      self.configure(bg=settings.PROGRAM_BG)
      self.user = user

      
      self.initialize_form()

      self.message = None

   
   def initialize_form(self):
      self.title = Label(self, text="Mijn profiel", bg=settings.PROGRAM_BG,font=("Arial", 16), fg='blue', anchor=W)
      self.title.place(x=10, y=10, height=40, width=130)

      self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG, anchor=W)
      self.first_name.place(relx=0.150, rely=0.200, height=20, width=120)

      self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG, anchor=W)
      self.last_name.place(relx=0.150, rely=0.250, height=20, width=120)

      self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG, anchor=W)
      self.email.place(relx=0.150, rely=0.300, height=20, width=120)

      self.role = Label(self, text='Rol:', bg=settings.PROGRAM_BG, anchor=W)
      self.role.place(relx=0.150, rely=0.350, height=20, width=120)

      self.first_name_box = Entry(self)
      self.first_name_box.insert(0, f'{self.user.first_name}')
      self.first_name_box.place(relx=0.250, rely=0.200, height=20, width=200)

      self.last_name_box = Entry(self)
      self.last_name_box.insert(0, f'{self.user.last_name}')
      self.last_name_box.place(relx=0.250, rely=0.250, height=20, width=200)

      self.email_box = Entry(self)
      self.email_box.insert(0, f'{self.user.email}')
      self.email_box.place(relx=0.250, rely=0.300, height=20, width=200)

      self.role = Label(self, text=f'{self.user.role}', bg=settings.PROGRAM_BG, anchor=W)
      self.role.place(relx=0.250, rely=0.350, height=20, width=200)

      self.save_button = Button(self, text="Opslaan", bg=settings.BUTTON_BG)
      self.save_button.place(relx=0.250, rely=0.400, height=30, width=200)
      self.save_button.configure(command=self.save_user)


      self.cancel_button = Button(self, text="Annuleer", bg=settings.WARNING_BUTTON_BG)
      self.cancel_button.place(relx=0.250, rely=0.470, height=30, width=200)
      self.cancel_button.configure(command=self.cancel)

      #change password
      self.password = Label(self, text="Nieuw wachtwoord", bg=settings.PROGRAM_BG, anchor=W)
      self.password.place(relx=0.550, rely=0.200, height=20, width=120)

      self.repeat_password = Label(self, text="Herhaal wachtwoord", bg=settings.PROGRAM_BG, anchor=W)
      self.repeat_password.place(relx=0.550, rely=0.250, height=20, width=120)

      self.password_box = Entry(self)
      self.password_box.configure(show="*")
      self.password_box.place(relx=0.700, rely=0.200, height=20, width=200)

      self.repeat_password_box = Entry(self)
      self.repeat_password_box.configure(show="*")
      self.repeat_password_box.place(relx=0.700, rely=0.250, height=20, width=200)

      self.save_password_button = Button(self, text="Wijzig wachtwoord", bg=settings.BUTTON_BG)
      self.save_password_button.place(relx=0.700, rely=0.300, height=30, width=200)
      self.save_password_button.configure(command=self.change_password)


   def save_user(self):
      Helper.clear_message(self)

      first_name = self.first_name_box.get()
      last_name = self.last_name_box.get()
      email = self.email_box.get()

      if not first_name or not last_name or not email:
         Helper.error_message(self, 'Niet alle velden zijn ingevuld')
         return

      if User.check_email_exists(email, self.user.userID):
         Helper.error_message(self, 'Dit emailadres is al in gebruik')
         return

      result = self.user.update_user(email, first_name, last_name)

      if result:
         Helper.success_message(self, 'Update succesvol')
      else:
         Helper.error_message(self, 'Update mislukt')


      
   def change_password(self):
      Helper.clear_message(self)

      new_password = self.password_box.get()
      repeat_password = self.repeat_password_box.get()



      if not new_password or len(new_password) < 4:
         Helper.error_message(self, 'Wachtwoord moet minstens 4 tekens bevatten.')
         return

      if new_password != repeat_password:
         Helper.error_message(self, 'Wachtwoorden komen niet overeen')
         return

      result = self.user.change_password(new_password)

      if not result:
         Helper.error_message(self, 'Update mislukt')
      else:
         Helper.success_message(self, 'Wachtwoord succesvol gewijzigd')
         self.password_box.delete("0",END)
         self.repeat_password_box.delete("0",END)

   def cancel(self):
      self.initialize_form()



