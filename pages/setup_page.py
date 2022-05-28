import tkinter as tk
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from mysql.connector import (connection)
import settings
from classes.db import Db
from classes.user import User
import settings

#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
#maak klasse active chain om keten lokaal te hebben staan en gearunits te kunnen ophalen etc

#class Active_chain:
#    def __init__(self):

chain_list = []

class Setup_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        #setup
        self.configure(bg=settings.PROGRAM_BG)
        self.user = user

        self.label_setup= Label(self, text="Choose setup" )
        #self.label_setup.pack(side = LEFT, fill = BOTH)
        self.label_setup.place(relx=0.1, rely = 0.1)


        self.box_setup = Listbox(self)
        self.box_setup.place(relx=0.1, rely = 0.2)
        self.select_setups
        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.pack(side=RIGHT, fill=BOTH)
        #sql_listbox_setup="SELECT setupName , setupDescription FROM setups;"


        #self.box_setup.config(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.config(command=self.box_setup.yview)


        self.label_setup_name = Label(self, text="Or enter new setup name:")
        self.label_setup_name.place(relx=0.1, rely=0.7)

        self.entry_newsetup= Entry(self, width= 20, bg= "white")
        self.entry_newsetup.place(relx=0.1,rely=0.75)


        self.label_setup_desc = Label(self, text="and setup description:")
        self.label_setup_desc.place(relx=0.1, rely=0.8)

        self.entry_newsetup_desc= Entry(self, width= 20, bg= "white")
        self.entry_newsetup_desc.place(relx=0.1,rely=0.85)


        self.but_cr_setup = Button(self, text="create setup", command=self.write_new_setup, pady=5)
        #self.but_cr_setup.pack(side = RIGHT, fill = BOTH)
        self.but_cr_setup.place(relx=0.1, rely=0.9)


#COLUMN2
        self.select_chains

        self.label_chain = Label(self, text="Choose Chain")
        # self.label_chain.pack()
        self.label_chain.place(relx=0.3, rely=0.1)


        self.box_chains = Combobox(self, values=chain_list)
        self.box_chains.place(relx=0.3, rely = 0.2)


#COLUMN3

        self.label_order = Label(self, text="Choose position")
        # self.label_chain.pack()
        self.label_order.place(relx=0.5, rely=0.1)

        self.box_order = Combobox(self)
        self.box_order.place(relx=0.5, rely = 0.2)


        self.but_pk_pos = Button(self, text="pick position", command=self.select_position, pady=5)
        self.but_pk_pos.place(relx=0.5, rely=0.9)


# COLUMN4

        self.label_gear = Label(self, text="Choose Gearunit")
        # self.label_chain.pack()
        self.label_gear.place(relx=0.7, rely=0.1)

        self.box_gear = Listbox(self)
        self.box_gear.place(relx=0.7, rely=0.2)

        self.but_pk_gear = Button(self, text="pick gear", command=self.add_gear, pady=5)
        self.but_pk_gear.place(relx=0.7, rely=0.9)







    def write_new_setup(self):
        db = Db()
        query ="INSERT INTO `sql11491613`.`setups` (`setupName`,`setupDescription`) VALUES (%s,%s);"
        data =(self.entry_newsetup.get(),self.entry_newsetup_desc.get())
        db.db_insert(query,data)


    def select_setups(self):
        db.cursor.execute("SELECT setupName , setupDescription FROM setups;")
        for x in db.cursor():
            self.box_setup.insert(END, x)

        self.select_setups

    def select_chains(self):
        db.cursor.execute("SELECT chainName from chains;")
        self.chain_list = []
        for x in db.cursor:
            self.chain_list.append(x)

    def select_position(self):
        picked_pos=self.but_pk_pos.anchor


    def get_setups(self ):
        db=Db()
        query="SELECT setupName , setupDescription FROM setups;"
        result=db.db_select(query)

        self.get_setups

    def add_gear(self):
        gear=self.box_gear.get()



'''

#freeSQL

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')


#remoteSQL
db = connection.MySQLConnection(user='Xpjf2Sfx1l', password='EZIFTyptKF',
                                host='37.59.55.185',
                                database='Xpjf2Sfx1l')
'''

'''
mycursor = db.cursor()

#hoofdvenster

win=Tk()
win.title("Setup window")
win.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")


setupvar = StringVar()
setuplabel = Label(win, textvariable=setupvar )
setuplabel.place(x = 100, y = 25)
# set label value
setupvar.set("Choose setup")


# listbox met setups
box_s = Listbox(win)
##listbox.pack(side=LEFT, fill=BOTH)
box_s.place(x = 100, y = 50)
scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=BOTH)
mycursor.execute("SELECT setupName , setupDescription FROM setups;")
for x in mycursor:
    box_s.insert(END, x)
box_s.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=box_s.yview)

#label setupname
setupvar = StringVar()
setuplabel = Label(win, textvariable=setupvar )
setuplabel.place(x = 100, y = 230)
setupvar.set("Or enter new setup name:")

#Entry Widget
entry= Entry(win, width= 20, bg= "white")
entry.place(x=100,y=250)

#button
def click():
    mycursor.execute("INSERT INTO `sql11491613`.`setups` (`setupName`) VALUES ('nu');")
c = Button(win, text="create setup", command=click, pady=5)
c.place(x=100,y=300)




#label ketens
chainvar = StringVar()
chainlabel = Label(win, textvariable=chainvar )
chainlabel.place(x = 300, y = 25)
# set label value
chainvar.set("Choose chain")

#haal ketens op uit database om te laten zien in combobox
mycursor.execute("SELECT chainName from chains")
data=[]
for x in mycursor:
    data.append(x)
box_c=Combobox(win, values=data)
box_c.place(x=300, y=50)

#button pick chain
def click_chain():
    picked_chain=ANCHOR
    sql=""
    mycursor.execute("")
but_pickchain = Button(win, text="pick chain", command=click_chain(), pady=5)
but_pickchain.place(x=300,y=300)



#message show chain elements
chainvar = StringVar()
showchain = Message(win, text="chain elements:")
showchain.place(x=300,y=80)


#label position
var_pos = StringVar()
label_pos = Label(win, textvariable=var_pos )
label_pos.place(x = 500, y = 25)
# set label value
var_pos.set("Choose gear position in chain")

#toon nummers
data=["1","2","3","4","5"]
cb=Combobox(win, values=data)
cb.place(x=500, y=50)

#button pick chain
def click_pos():
    picked_pos=ANCHOR
    sql=""
    mycursor.execute("")
but_pickpos = Button(win, text="pick position", command=click_pos, pady=5)
but_pickpos.place(x=500,y=300)




#label gearunits
gearvar = StringVar()
gearlabel = Label(win, textvariable=gearvar )
gearlabel.place(x = 700, y = 25)
# set label value
gearvar.set("Choose gearunit")

#haal gearunits op uit database om te laten zien in combobox
mycursor.execute("SELECT gearunitName from gearunits")
data=[]
for x in mycursor:
    data.append(x)
cb=Combobox(win, values=data)
cb.place(x=700, y=50)

#button pick chain
def click_gear():
    picked_pos=ANCHOR
    sql=""
    mycursor.execute("")
but_pickgear = Button(win, text="pick position", command=click_gear, pady=5)
but_pickgear.place(x=700,y=300)



win.mainloop()

'''
