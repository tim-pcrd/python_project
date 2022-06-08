import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from mysql.connector import (connection)
from classes.db import Db
from classes.user import User
import settings
import classes.setup
import bcrypt




db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                 host='35.157.16.43',
                                 database='sql11491613')

mycursor = db.cursor()


#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python



activechain=classes.setup.ActiveChain()
print(activechain)
activesetup=classes.setup.ActiveSetup()
print(activesetup)


class Setup_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.label_welcome = Label(self, text="Welkom bij de Setup Manager. Hier kan je een setup kiezen of maken, en je chains definieren die je wilt gebruiken.")
        self.label_welcome.place(relx=0.1, rely=0.05)

        #setup
        self.configure(bg=settings.PROGRAM_BG)
        self.user = user




        self.label_setup= Label(self, text="1) Kies setup:" )
        #self.label_setup.pack(side = LEFT, fill = BOTH)
        self.label_setup.place(relx=0.1, rely = 0.15)


        self.box_setup = Listbox(self)
        self.box_setup.place(relx=0.1, rely = 0.2)

        self.get_setups()

        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.pack(side=RIGHT, fill=BOTH)
        #sql_listbox_setup="SELECT setupName , setupDescription FROM setups;"


        #self.box_setup.config(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.config(command=self.box_setup.yview)


        self.label_setup_name = Label(self, text="Of geef nieuwe setup naam in:")
        self.label_setup_name.place(relx=0.1, rely=0.5)

        self.entry_newsetup= Entry(self, width= 20, bg= "white")
        self.entry_newsetup.place(relx=0.1,rely=0.55)


        self.label_setup_desc = Label(self, text="met setup description:")
        self.label_setup_desc.place(relx=0.1, rely=0.6)

        self.entry_newsetup_desc= Entry(self, width= 20, bg= "white")
        self.entry_newsetup_desc.place(relx=0.1,rely=0.65)


        self.but_cr_setup = Button(self, text="maak setup", command=self.write_new_setup, pady=5)
        #self.but_cr_setup.pack(side = RIGHT, fill = BOTH)
        self.but_cr_setup.place(relx=0.1, rely=0.7)

        self.but_pk_setup = Button(self, text="pick setup", command=self.pick_setup, pady=5)
        self.but_pk_setup.place(relx=0.1, rely=0.8)


        self.label_save_setup = Label(self, text="Sla setup op:")
        #self.label_save_setup.place(relx=0.9, rely=0.85)

        self.but_save_setup = Button(self, text="save setup", command=self.save_setup, pady=5)
        self.but_save_setup.place(relx=0.9, rely=0.9)


#COLUMN2


        self.label_chain = Label(self, text="2) Kies Chain:")
        # self.label_chain.pack()
        self.label_chain.place(relx=0.3, rely=0.15)

        self.box_chains = Listbox(self)
        self.box_chains.place(relx=0.3, rely = 0.2)

        self.get_chains()

        self.label_chain_name = Label(self, text="Of geef nieuwe chain naam in:")
        self.label_chain_name.place(relx=0.3, rely=0.5)

        self.entry_newchain= Entry(self, width= 20, bg= "white")
        self.entry_newchain.place(relx=0.3,rely=0.55)

        self.but_cr_chain = Button(self, text="maak chain", command=self.write_new_chain, pady=5)
        #self.but_cr_setup.pack(side = RIGHT, fill = BOTH)
        self.but_cr_chain.place(relx=0.3, rely=0.6)

        self.but_update_chain = Button(self, text="update chain", command=self.update_chain, pady=5)
        #self.but_cr_setup.pack(side = RIGHT, fill = BOTH)
        self.but_update_chain.place(relx=0.3, rely=0.7)



        self.but_pk_chain = Button(self, text="pick chain", command=self.pick_chain, pady=5)
        self.but_pk_chain.place(relx=0.3, rely=0.8)




#COLUMN3

        self.label_order = Label(self, text="3) Kies positie:")
        # self.label_chain.pack()
        self.label_order.place(relx=0.5, rely=0.15)

        data = [1,2,3,4,5]
        self.box_order = Combobox(self, values=data)
        self.box_order.place(relx=0.5, rely = 0.2)

        chain_gearunits="gearunits"
        self.box_chain_gearunits = Message(self, width=200, text=activechain )
        self.box_chain_gearunits.place(relx=0.5, rely = 0.3)


        self.label_posbut= Label(self, text="kies positie van gearunit in chain:")
        self.label_posbut.place(relx=0.5, rely=0.75)

        self.but_pk_pos = Button(self, text="pick positie", command=self.pick_position, pady=5)
        self.but_pk_pos.place(relx=0.5, rely=0.8)


# COLUMN4

        self.label_gear = Label(self, text="4) Kies Gearunit:")
        # self.label_chain.pack()
        self.label_gear.place(relx=0.7, rely=0.15)

        self.box_gear = Listbox(self)
        self.box_gear.place(relx=0.7, rely=0.2)
        self.get_gearunits()


        self.label_gearbut= Label(self, text="zet gear op gekozen chain positie:")
        self.label_gearbut.place(relx=0.7, rely=0.75)

        self.but_pk_gear = Button(self, text="pick gear", command=self.add_gear, pady=5)
        self.but_pk_gear.place(relx=0.7, rely=0.8)





#------------selecteer----------------------

    def pick_setup(self):

        global picked_setup
        global activesetup
        picked_setup=0
        activesetup = classes.setup.ActiveSetup()
        ps=self.box_setup.curselection()[0]
        mycursor.execute("SELECT  *  FROM setups ORDER BY setupID ASC;")

        i = 0
        for x in mycursor:
            if i == ps:
                picked_setup = x
            i += 1

        #activesetup.load_setup(picked_setup)
        activesetup.setupID=picked_setup[0]
        activesetup.setupName=picked_setup[1]
        activesetup.setupDescription=picked_setup[2]

        print(activesetup)# ter controle








    def pick_chain(self):
        global activechain
        activechain = classes.setup.ActiveChain()       #instantie maken van de Activechain klasse
        pc=self.box_chains.curselection()[0]+1              #de keuze van de listbox nemen, geeft tuple
        #picked_chain=pc[0]+1                            # eerste waarde van tuple kiezen en de int verhogen met 1 omdat eerste chain chainID 1 heeft

        activechain.select_chain(pc)          #de chainID doorgeven aan de select_chain methode

        self.box_chain_gearunits.update()
        print(activechain) #ter controle

    def pick_position(self):
        global picked_position
        pp=self.box_order.get()
        picked_position = int(pp)
        print(picked_position)

# ----------wegschrijven------------------

    def add_gear(self):
        global picked_position
        global gearlist
        pg = self.box_gear.curselection()[0]  # =int
        mycursor.execute("SELECT  gearunitName  FROM gearunits;")
        i = 0
        for x in mycursor:
            if i == pg:
                picked_gear = x
            i += 1
        picked_gear_name = picked_gear[0]
        print(picked_gear_name)
        if picked_position == 1:
            activechain.pos1 = picked_gear_name
        elif picked_position == 2:
            activechain.pos2 = picked_gear_name
        elif picked_position == 3:
            activechain.pos3 = picked_gear_name
        elif picked_position == 4:
            activechain.pos4 = picked_gear_name
        elif picked_position == 5:
            activechain.pos5 = picked_gear_name


    def save_setup(self):
        IDlist=[]
        mycursor.execute("SELECT setupID FROM setups;")
        for x in mycursor:
            IDlist.append(x)
        if activesetup.setupID in IDlist:
            self.update_setup()
        else:
            self.write_setup()

    def write_setup(self):
        db = Db()
        query1 ="INSERT INTO `setups` (`setupName`,`setupDescription`) VALUES (%s,%s);"
        data1 =(activesetup.setupName,activesetup.setupDescription)
        #query2=
        #data2=


        db.db_insert(query1,data1)

        self.box_setup.update()

    def update_setup(self):
        db = Db()
        query1 ="UPDATE `setups` SET `setupName` = '%s', `setupDescription` = '%s' WHERE(`setupID` = '%s');"
        data1 =(activesetup.setupName,activesetup.setupDescription,activesetup.setupID)
        #query2=
        #data2=


        db.db_insert(query1,data1)

        self.box_setup.update()


    def update_chain(self):
        pass


    def write_new_setup(self):
        db = Db()
        query ="INSERT INTO `setups` (`setupName`,`setupDescription`) VALUES (%s,%s);"
        setupName=self.entry_newsetup.get()
        setupDescription=self.entry_newsetup_desc.get()
        data =(setupName,setupDescription)
        db.db_insert(query,data)


        mycursor.execute("SELECT setupID FROM setups ORDER BY setupID DESC LIMIT 1;")
        setupID=100
        for x in mycursor:
            setupID=x[0]+1
        activesetup.setupID=setupID
        activesetup.setupName=setupName
        activesetup.setupDescription=setupDescription
        print(activesetup)

        self.entry_newsetup.delete(0, 'end')
        self.entry_newsetup_desc.delete(0, 'end')
        self.box_setup.delete(0, 'end')
        self.get_setups()


    def write_new_chain(self):
        db = Db()
        query ="INSERT INTO `sql11491613`.`chains` (`chainName`) VALUES (%s);"
        data =[self.entry_newchain.get()]
        db.db_insert(query,data)
        self.entry_newchain.delete(0, 'end')
        self.box_chains.delete(0, 'end')
        #self.box_chains.
        self.get_chains()


#-------haal info uit db voor weergave in list/comboboxes-------------

    #setups ophalen uit database
    def get_setups(self):
        self.box_setup.delete(0, END)
        mycursor.execute("SELECT setupID, setupName , setupDescription FROM setups;")
        for x in mycursor:
            self.box_setup.insert(END, x)


    #chains ophalen uit database
    def get_chains(self):
        mycursor.execute("SELECT chainName  FROM chains;")
        for x in mycursor:
            self.box_chains.insert(END, x)

    #alle gearunits ophalen uit database
    def get_gearunits(self):
        mycursor.execute("SELECT gearunitID, gearunitName  FROM gearunits;")
        for x in mycursor:
            self.box_gear.insert(END, x)

#---------------refreshes--------------

    def refresh_s(self):
        pass

    def refresh_c(self):
        pass

    def refresh_g(self):
        pass






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


