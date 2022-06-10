import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from mysql.connector import (connection)
from classes.db import Db
from classes.user import User
import settings
import classes.setup
from classes.project_session import ActiveSession
import pages.setup_page as stppg

from mysql.connector import (connection)

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')



# db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
#                                  host='35.157.16.43',
#                                  database='sql11491613')
mycursor = db.cursor()


activesession=classes.project_session.ActiveSession()


class Session_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        #setup
        self.configure(bg=settings.PROGRAM_BG)
        self.user = user

        self.label_activesession = tk.Label(self, fg='black', font=('Arial', 12), width=10, text="Active Session")
        self.label_activesession.pack()

        self.var1 = tk.StringVar()
        self.label_session = tk.Label(self, bg='yellow', fg='black', font=('Arial', 12), width=10, textvariable=self.var1)
        self.label_session.pack()

        #select session
        self.but_select_session = tk.Button(self, text='Select session', width=20, height=2, command=self.selected_session)
        self.but_select_session.pack()

        # Copy existing session:
        self.b3 = tk.Button(self, text='Copy existing session', width=20, height=2)  # command=
        self.b3.pack()
        self.box_session = tk.Listbox(self)
        self.box_session.pack()
        self.add_items_listbox()

        self.label_setup= Label(self, text="Kies setup:" )
        #self.label_setup.pack(side = LEFT, fill = BOTH)
        self.label_setup.pack()



        self.box_setup = Combobox(self, values=setuplist)
        self.box_setup.pack()





        self.entry_newsession= Entry(self, width= 20, bg= "white")
        self.entry_newsession.pack()

        # Create a new session:
        self.b2 = tk.Button(self, text='Create new session', width=20, height=2 ,  command=self.write_session )
        self.b2.pack()




    # Add more items to the LISTBOX:
    def add_items_listbox(self):
        # db=Db()
        # query="SELECT sessionID FROM sessions;"
        # data=[]
        # db.db_select(query,data)
        # for x in db:
        #     self.lb.insert('end', x)
        # self.lb.pack()


        mycursor.execute("SELECT sessionID, sessionName FROM sessions;")
        for x in mycursor:
           self.box_session.insert('end', x)
        self.box_session.pack()


    def selected_session(self):
        global selected_session
        selected_session = self.box_session.get(self.box_session.curselection())
        self.var1.set(selected_session)
        print(selected_session)
        activesession.load_session(selected_session)
        print(activesession)

    def write_session(self):
        db = Db()
        query ="INSERT INTO `sessions` (`sessionName`,`projectID`,`setupID`,`date`,`sessiontypeID`) VALUES (%s,%s,%s,%s,%s);"
        data =(activesession.sessionName,activesession.projectID,activesession.setupID,activesession.date,activesession.sessiontypeID)
        db.db_insert(query,data)
        self.box_setup.update()


    def copy_session(self):
        global selected_session
        activesession.load_session(selected_session)
        self.write_session()
        activesession.load_newest_session()


    def write_new_session(self):
        sessionName=self.entry_newsession.get()
        activesession.add_session( sessionName, activesession.projectID, activesession.setupID)

    def fill_combobox_setups(self):
        stps=stppg.Setup_Page.get_setups(self)
        setuplist=[]
        for x in stps:
            setuplist.append(x)
        return setuplist


'''
CODE VAN SANNE:


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