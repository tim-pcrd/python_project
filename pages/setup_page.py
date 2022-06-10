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



#aanmaak van de instanties die de actieve setup/chain gaan bevatten

activesetup=classes.setup.ActiveSetup()
print(activesetup)
activechain=classes.setup.ActiveChain()
print(activechain)


# aanmaak van het venster
class Setup_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        # setup
        self.configure(bg=settings.PROGRAM_BG)
        self.user = user


#COLUMN1

        self.label_welcome = Label(self, text="Welkom bij de Setup Manager. Hier kan je een setup kiezen of maken, en je chains definieren die je wilt gebruiken.")
        self.label_welcome.place(relx=0.1, rely=0.05)


        self.label_setup= Label(self, text="1) Kies setup:" )
        self.label_setup.place(relx=0.1, rely = 0.15)


        self.box_setup = Listbox(self)
        self.box_setup.place(relx=0.1, rely = 0.2)

        #schrijf setups in listbox
        self.get_setups()


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
        self.but_pk_setup.place(relx=0.1, rely=0.85)


        # self.label_save_setup = Label(self, text="Sla setup op:")
        # #self.label_save_setup.place(relx=0.9, rely=0.85)
        #
        # self.but_save_setup = Button(self, text="save setup", command=self.update_setup, pady=5)
        # self.but_save_setup.place(relx=0.9, rely=0.9)


#COLUMN2


        self.label_chain = Label(self, text="2) Kies Chain:")
        # self.label_chain.pack()
        self.label_chain.place(relx=0.3, rely=0.15)

        self.box_chains = Listbox(self)
        self.box_chains.place(relx=0.3, rely = 0.2)

        #schrijf chain in listbox
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
        self.but_pk_chain.place(relx=0.3, rely=0.85)




#COLUMN3

        self.label_order = Label(self, text="3) Kies positie:")
        # self.label_chain.pack()
        self.label_order.place(relx=0.5, rely=0.15)

        data = [1,2,3,4,5]
        self.box_order = Combobox(self, values=data)
        self.box_order.place(relx=0.5, rely = 0.2)

        #laadt de activesetup en activechiain inhoud naar een message
        self.load_messages()

        self.label_posbut= Label(self, text="kies positie van gearunit in chain:")
        self.label_posbut.place(relx=0.5, rely=0.8)

        self.but_pk_pos = Button(self, text="pick positie", command=self.pick_position, pady=5)
        self.but_pk_pos.place(relx=0.5, rely=0.85)


# COLUMN4

        self.label_gear = Label(self, text="4) Kies Gearunit:")
        # self.label_chain.pack()
        self.label_gear.place(relx=0.7, rely=0.15)

        self.box_gear = Listbox(self)
        self.box_gear.place(relx=0.7, rely=0.2)
        self.get_gearunits()


        self.label_gearbut= Label(self, text="zet gear op gekozen chain positie:")
        self.label_gearbut.place(relx=0.7, rely=0.8)

        self.but_pk_gear = Button(self, text="pick gear", command=self.add_gear, pady=5)
        self.but_pk_gear.place(relx=0.7, rely=0.85)





#------------selecteer methodes----------------------

    #haalt setups op uit database en zet degene die je in listbox kiest in de activesetup
    def pick_setup(self):

        global picked_setup
        global activesetup
        picked_setup=0
        activesetup = classes.setup.ActiveSetup()
        ps=self.box_setup.curselection()[0]
        setuplist=activesetup.get_setuplist()

        i = 0
        for x in setuplist:
            if i == ps:
                picked_setup = x
            i += 1


        activesetup.setupID=picked_setup[0]
        activesetup.setupName=picked_setup[1]
        activesetup.setupDescription=picked_setup[2]

        chainlist_concerned=self.get_chains_concerned()

        self.box_show_setup.destroy()
        self.box_show_chain.destroy()
        self.load_messages()
        print(activesetup)# ter controle



    #haalt chains op uit database en zet degene die je in listbox kiest in de activechain
    def pick_chain(self):
        global activechain
        activechain = classes.setup.ActiveChain()           #instantie maken van de Activechain klasse
        pc=self.box_chains.curselection()[0]+1              #de keuze van de listbox nemen, geeft tuple
                                                            #eerste waarde van tuple kiezen en de int verhogen
                                                            # met 1 omdat eerste chain chainID 1 heeft en listboxkeuze 0.

        activechain.select_chain(pc)                        #de chainID doorgeven aan de select_chain methode die de activeschain invult

        self.box_show_setup.destroy()                       #oude messages weghalen
        self.box_show_chain.destroy()
        self.load_messages()                                #nieuwe messages laden om inhoud ativesetup en activechain weer te geven

        print(activechain)                                  #ter controle


    #positie van gearunit tijdelijk opslaan
    def pick_position(self):
        global picked_position
        pp=self.box_order.get()
        picked_position = int(pp)
        print(picked_position)






# ----------wegschrijven------------------



    # def save_setup(self):
    #     current_setupID = activesetup.setupID
    #
    #     if activesetup.setupID == None:
    #         self.write_setup()
    #     else:
    #         self.update_setup(current_setupID)
    #
    #
    # def write_setup(self):
    #     db = Db()
    #     query1 ="INSERT INTO `setups` (`setupName`,`setupDescription`) VALUES (%s,%s);"
    #     data1 =(activesetup.setupName,activesetup.setupDescription)
    #     db.db_insert(query1,data1)
    #
    #     self.box_setup.update()

    def update_setup(self):
        db = Db()
        query1 ="UPDATE setups SET setupName = %s, setupDescription = %s WHERE(setupID = %s);"
        data1 =(activesetup.setupName,activesetup.setupDescription,activesetup.setupID)

        db.db_insert(query1,data1)

        self.box_setup.delete(0, tk.END)
        self.get_setups()


    def write_new_setup(self):
        #niewe setup wegschrijven
        db = Db()
        query ="INSERT INTO `setups` (setupName,setupDescription) VALUES (%s,%s);"
        setupName=self.entry_newsetup.get()
        setupDescription=self.entry_newsetup_desc.get()
        data =(setupName,setupDescription)
        db.db_insert(query,data)

        #nieuwe setup ophalen
        db2=Db()
        query2="SELECT * FROM setups ORDER BY setupID DESC LIMIT 1;"
        data2=[]
        new_setup=db2.db_select(query2, data2)
        print(new_setup)

        #setupID uit setup halen
        setupID=100
        for x in new_setup:
            setupID=x[0]

        #active setup updaten
        activesetup.setupID=setupID
        activesetup.setupName=setupName
        activesetup.setupDescription=setupDescription
        print(activesetup)

        #entries en list refreshen
        self.entry_newsetup.delete(0, 'end')
        self.entry_newsetup_desc.delete(0, 'end')
        self.box_setup.delete(0, tk.END)
        self.get_setups()

    #wegscrijven van nieuwe chain en refreshen van chain listbox
    def write_new_chain(self):
        db = Db()
        query ="INSERT INTO `chains` (`chainName`) VALUES (%s);"
        data =[self.entry_newchain.get()]
        db.db_insert(query,data)

        self.entry_newchain.delete(0, 'end')
        self.box_chains.delete(0, tk.END)
        self.get_chains()

    #advanced functie/niet operationeel
    def update_chain(self):


        db = Db()
        query ="UPDATE `chains` SET `chainName` = '%s' WHERE(`chainID` = '%s');"
        data =[activechain.chainName,activechain.chainID]
        db.db_insert(query,data)

        #hiervoor moet de ketenID mee in de klasse weggeschreven zijn? + hoe de juiste entry in db opzoeken om up te daten?
        db = Db()
        query ="UPDATE `setup_chain` SET `chainID` = '%s' WHERE(`setupID` = '%s' AND channel =%s );"
        data =[activechain.chainID[0],activesetup.setupID]
        db.db_insert(query,data)

        self.entry_newchain.delete(0, 'end')
        self.box_chains.delete(0, tk.END)
        self.get_chains()



    #zet gear in active chain
    def add_gear(self):
        global picked_position
        global gearlist
        pg = self.box_gear.curselection()[0]  # =int
        gearlist=activesetup.get_gearlist()
        i = 0
        for x in gearlist:
            if i == pg:
                picked_gear = x
            i += 1
        picked_gear_name = picked_gear[1]
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

        self.box_show_setup.destroy()
        self.box_show_chain.destroy()
        self.load_messages()



#-------haal info uit db voor weergave in list/comboboxes-------------

    #setups ophalen uit database en in listbox printen
    def get_setups(self):
        self.box_setup.delete(0, tk.END)
        setuplist=activesetup.get_setuplist()
        for x in setuplist:
            self.box_setup.insert(END ,x)

    # #chains ophalen uit database en in listbox printen
    def get_chains(self):
        self.box_chains.delete(0, tk.END)
        chainlist=activesetup.get_chainlist()
        for x in chainlist:
            self.box_chains.insert(END, x)

    #chains van een bepaalde setup ophalen uit database en in listbox printen
    def get_chains_concerned(self):
        activesetupID=activesetup.setupID
        print(activesetupID)
        self.box_chains.delete(0, tk.END)
        chainlist_concerned=activesetup.get_chainlist_concerned(activesetupID)
        print(chainlist_concerned)
        for x in chainlist_concerned:
            self.box_chains.insert(END ,x)

    #gearunits ophalen en in listbox printen
    def get_gearunits(self):
        gearlist=activesetup.get_gearlist()
        for x in gearlist:
            self.box_gear.insert(END, x)

    #messages weergeven die de inhoude van de instanties activeseetup en activechain laten zien
    def load_messages(self):

        self.box_show_setup = Message(self, width=200, text=activesetup )
        self.box_show_setup.place(relx=0.5, rely = 0.3)

        self.box_show_chain = Message(self, width=200, text=activechain )
        self.box_show_chain.place(relx=0.5, rely = 0.5)











