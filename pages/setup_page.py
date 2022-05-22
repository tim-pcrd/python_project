import tkinter as tk
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from mysql.connector import (connection)
import settings


#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
#maak klasse active chain om keten lokaal te hebben staan en gearunits te kunnen ophalen etc

#class Active_chain:
#    def __init__(self):



#freeSQL

db = connection.MySQLConnection(user='sql11491613', password='eWFcPv5Ndt',
                                host='35.157.16.43',
                                database='sql11491613')
'''

#remoteSQL
db = connection.MySQLConnection(user='Xpjf2Sfx1l', password='EZIFTyptKF',
                                host='37.59.55.185',
                                database='Xpjf2Sfx1l')
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
root = Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = Text(root, height=5, width=52)

# Create label
l = Label(root, text="Fact of the Day")
l.config(font=("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = Button(root, text="Next", )

# Create an Exit button.
b2 = Button(root, text="Exit",
            command=root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)

tk.mainloop()
tk.Menu



root = Tk()
root.geometry("300x300")
root.title(" Q&A ")


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if (INPUT == "120"):
        Output.insert(END, 'Correct')
    else:
        Output.insert(END, "Wrong answer")


l = Label(text="What is 24 * 5 ? ")
inputtxt = Text(root, height=10,
                width=25,
                bg="light yellow")

Output = Text(root, height=5,
              width=25,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

'''