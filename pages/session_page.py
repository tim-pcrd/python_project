import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from mysql.connector import (connection)
from classes.db import Db
from classes.user import User
import settings
import classes.setup

from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')
mycursor = db.cursor()


class Session_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.var1 = tk.StringVar()
        self.l = tk.Label(self, bg='yellow', fg='black', font=('Arial', 12), width=10, textvariable=self.var1)
        self.l.pack()

        self.b1 = tk.Button(self, text='Select session', width=20, height=2, command=self.selected_session)
        self.b1.pack()

        self.lb = tk.Listbox(self)
        self.lb.pack()

        # Create a new session:

        self.b2 = tk.Button(self, text='Create new session', width=20, height=2)  # command=
        self.b2.pack()

    # Copy existing session:
        self.b3 = tk.Button(self, text='Copy existing session', width=20, height=2)  # command=
        self.b3.pack()

        self.add_items_listbox()


    # Add more items to the LISTBOX:
    def add_items_listbox(self):
        mycursor.execute("SELECT sessionID FROM sessions;")
        for x in mycursor:
            self.lb.insert('end', x)
        self.lb.pack()


    def selected_session(self):
        value = self.lb.get(self.lb.curselection())
        self.var1.set(value)


'''
#Create WINDOW "Session":
window = tk.Tk()
window.title('Session')
window.geometry('500x500')


#Create LABEL which shows selected session:
var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', fg='black', font=('Arial', 12), width=10, textvariable=var1)
l.pack()


def selected_session():
    value = lb.get(lb.curselection())
    var1.set(value)


#Create a BUTTON to select session:
b1 = tk.Button(window, text='Select session', width=20, height=2, command=selected_session)
b1.pack()


#TEST;                  Information from database needed!
test = [11, 22, 33, 44]
test_var = tk.StringVar(value=test)


#Create a LISTBOX:
lb = tk.Listbox(window, listvariable=test_var)
lb.pack()


#Create a new session:
b2 = tk.Button(window, text='Create new session', width=20, height=2) #command=
b2.pack()

#Copy existing session:
b3 = tk.Button(window, text='Copy existing session', width=20, height=2) #command=
b3.pack()


#Add more items to the LISTBOX:
mycursor.execute("SELECT sessionID FROM sessions;")
for x in mycursor:
    lb.insert('end', x)
lb.pack()


window.mainloop()

'''