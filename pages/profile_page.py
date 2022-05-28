from email import message
from tkinter import *
from classes.db import Db
from classes.user import User
import settings

class Profile_Page(Frame):
   def __init__(self, root, width, height, user: User):
      super().__init__(root, width=width, height=height)

      self.configure(bg=settings.PROGRAM_BG)
      self.user = user

      self.first_name = Label(self, text="Voornaam:", bg=settings.PROGRAM_BG)
      self.first_name.place(relx=0.100, rely=0.100, height=20, width=120)

      self.last_name = Label(self, text="Familienaam:", bg=settings.PROGRAM_BG)
      self.last_name.place(relx=0.100, rely=0.150, height=20, width=120)

      self.email = Label(self, text="Email:", bg=settings.PROGRAM_BG)
      self.email.place(relx=0.100, rely=0.200, height=20, width=120)

      self.first_name_box = Entry(self)
      self.first_name_box.insert(0, f'{self.user.first_name}')
      self.first_name_box.place(relx=0.200, rely=0.100, height=20, width=150)

      self.last_name_box = Entry(self)
      self.last_name_box.insert(0, f'{self.user.last_name}')
      self.last_name_box.place(relx=0.200, rely=0.150, height=20, width=150)

      self.email_box = Entry(self)
      self.email_box.insert(0, f'{self.user.email}')
      self.email_box.place(relx=0.200, rely=0.200, height=20, width=150)

      self.save_button = Button(self, text="Opslaan", bg=settings.BUTTON_BG)
      self.save_button.place(relx=0.200, rely=0.250, height=30, width=150)
      self.save_button.configure(command=self.save_user)


      #change password
      self.password = Label(self, text="Nieuw wachtwoord", bg=settings.PROGRAM_BG)
      self.password.place(relx=0.600, rely=0.100, height=20, width=150)

      self.repeat_password = Label(self, text="Herhaal wachtwoord", bg=settings.PROGRAM_BG)
      self.repeat_password.place(relx=0.600, rely=0.150, height=20, width=150)

      self.password_box = Entry(self)
      self.password_box.configure(show="*")
      self.password_box.place(relx=0.750, rely=0.100, height=20, width=150)

      self.repeat_password_box = Entry(self)
      self.repeat_password_box.configure(show="*")
      self.repeat_password_box.place(relx=0.750, rely=0.150, height=20, width=150)

      self.save_button = Button(self, text="Wijzig wachtwoord", bg=settings.BUTTON_BG)
      self.save_button.place(relx=0.750, rely=0.200, height=30, width=150)
      self.save_button.configure(command=self.change_password)

      self.message = None


   def save_user(self):
      first_name = self.first_name_box.get()
      last_name = self.last_name_box.get()
      email = self.email_box.get()
      result = self.user.update_user(email, first_name, last_name)

      if result and self.message:
         self.message.place_forget()


      
   def change_password(self):
      if self.message:
            self.message.place_forget()

      new_password = self.password_box.get()
      repeat_password = self.repeat_password_box.get()



      if not new_password or len(new_password) < 4:
         self.error_message('Wachtwoord moet minstens 4 tekens bevatten.')
         return

      if new_password != repeat_password:
         self.error_message('Wachtwoorden komen niet overeen.')
         return

      result = self.user.change_password(new_password)

      if not result:
         self.error_message('Update mislukt')
      elif self.message:
         self.message.place_forget()


   def error_message(self, message):
      self.message = Label(self, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12))
      self.message.place(relx=0.100, rely=0.700, height=40, width=400)



