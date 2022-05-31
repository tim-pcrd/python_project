#eerste experiment met klasses om te zien of we ze wel nodig hebben
#klasses met hoofdletter
#lijsten zonder hoofdletter

class Gear:

    def __init__(self, idGear, naam, keten):
        self.idGear = idGear
        self.naam = naam
        self.keten = "none"
        self.knoppen = []

    def toon_knoppen(self):
        for x in self.knoppen:
            print(x)

    def voeg_control_toe(self, control):
        self.knoppen.append(control)

    def __str__(self):

        return "Gearid:\t\t{} \nnaam:\t\t{} \nketen:\t\t{} \nknoppen:\t{}\n".format(self.idGear, self.naam, self.keten, self.knoppen)


class Control:

    def __init__(self, idControl, naam, type):
        self.idControl=idControl
        self.naam=naam
        self.type=type

    def __str__(self):
        return "Control ID:\t{} \nnaam:\t\t{} \ntype:\t\t{}".format(self.idControl, self.naam, self.type)




#klasse Keten met benoeming en een lijst 'gearseq' meegegeven
class Keten:

    def __init__(self, idKeten, naam, gearseq):
        self.idKeten=idKeten
        self.naam = naam
        self.gearseq=gearseq
        self.keteninfo=""


    def __str__(self):
        return "Keten ID: {} naam {} \nGearunits {}\nKeten info:".format(self.idKeten, self.naam, self.gearseq, self.keteninfo)


#---------------------------------------------
# info


rotary="rotary"
switch="switch"
gain=Control("c1","gain",rotary)
phantom=Control("c2","phantom",switch)

controls_comp=["tresh","ratio","attack","release",gain]
controls_eq=["freqLo","Qlo","gainLo","freqMid","Qmid","gainMid","freqHi","Qhi","gainHi",]
controls_pre=["gain","volume",phantom]


g1=Gear("g1","API 2500 compressor","CH1+2")
g1.voeg_control_toe(controls_comp)
g2=Gear("g2","Aphex Aural Exciter","LR")
g3=Gear("g3","FunkyFish SSL G-Gomp","LR")
g4=Gear("g4","Vintech Stereo Pre-amp/EQ","LR")
g5=Gear("g5","Aphex Stereo EQ","LR")

gearlist=[g1,g2,g3,g4,g5]


keten1=[1,g3,g4]
keten2=[2,g2,g1]
keten3=[]


K1=Keten("k1","Kanaal1",keten1)
K2=Keten("k2","Kanaal2",keten1)
K3=Keten("k3","Kanaal3",keten1)

#lijst met ketens. een keten is ook een lijst, dus uiteindelijk een lijst met lijsten
ketens=[keten1,keten2,keten3]

#lijst instances van klasse Keten
Ketens=[K1,K2,K3]


def write_gear_keten():
    for k in ketens:
        for x in gearlist:
            if x in k:
                str_k=str(k[0])
                x.keten = "keten"+str_k


write_gear_keten()

#-------------------------------------
#hoofdprogramma

def toon_gearlist():
    print("gearlist:")
    for x in gearlist:
        print(x)
        if x==type(list):
            for y in x:
                print(y.naam)
        print()
    print("-----gearlist END------\n")

def toon_Ketens():
    print("overzicht ketens:")
    for x in ketens:
        for y in x:
            print(y)


'''def maak_keten():
    print("maak keten:")
    for x in Ketens:
        print(x.naam+"(ID="+x.idKeten+")")

    ketenkeuze=input("geef keten ID in:")
    for y in Ketens:
        if ketenkeuze==y.idKeten:
           ketenlijst=list(y.gearseq)


    print("kies een outboard gear unit")
    for x in gearlist:
        print(x.naam+"(ID="+x.idGear+")")
    gearkeuze=input("geef ID in:")
    for x in gearlist:
        if gearkeuze==x.idGear:
            ketenlijst.append(x)
            y=Keten(y.idKeten,y.naam,ketenlijst)'''

def maak_keten():
    keuze_k=""
    keuze_g=""
    while not keuze_k == "n":

        print("maak keten:")
        for x in Ketens:
            print(x.naam+"(ID="+x.idKeten+")")
        ketenkeuze=input("geef keten ID in:")
        for y in Ketens:
            if ketenkeuze==y.idKeten:
                ketenlijst=list(y.gearseq)
        keuze_k = input("wil je nog een keten aanpassen? (y/n)")


        print("kies een outboard gear unit")
        for x in gearlist:
            print(x.naam+"(ID="+x.idGear+")")
        gearkeuze=input("geef ID in:")
        for x in gearlist:
            if gearkeuze==x.idGear:
                ketenlijst.append(x)
                y=Keten(y.idKeten,y.naam,ketenlijst)
        keuze_g=input("wil je nog een gearunit toevoegen? (y/n)")

def menu():
    print("je kan kiezen uit")
    print("1: Toon gearlijst")
    print("2: maak keten")
    print("3: toon ketens")
    print("4: ")
    print("5: ")
    print("6: ")

menu()
invoer = input("Wat wil je doen? geef het nummer in of stop om te stoppen")
print()
while(not invoer == "stop"):
    if(invoer == "1"):
        toon_gearlist()

    elif(invoer == "2"):

        toon_Ketens()

    elif(invoer == "3"):
        maak_keten()
    elif(invoer == "4"):
        pass
    elif(invoer == "5"):
        pass
    elif(invoer == "6"):
        pass
    menu()
    invoer = input("Wat wil je doen? geef het nummer in of stop om te stoppen")


