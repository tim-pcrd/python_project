from tkinter import Frame, Label, Message
from classes.user import User
import settings


class Home_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)

        self.configure(bg=settings.PROGRAM_BG)

        # self.name_label = Label(self, text=f'Hallo {user.first_name}', bg=settings.PROGRAM_BG, font=("Arial", 13), fg='blue')
        # self.name_label.place(x=5, y=10, height=20, width=120)


        var_uitleg =("\n"
        "Beste muziek enthousiast, \n\n " \
        "Je bent momenteel op de juiste plak als je werkt in een muziekstudio en handig een snapshot van " \
        "je gebruikte configuratie wilt oplaan en later weer wilt uitlezen om een ‘recall’ te maken.\n " \
        "Je maakt een project( muzikant/album/…) aan, en daarna een sessie (opname/mix/mastering).\n" \
        "Hierin houd je bij welke ‘setup’ je hebt gebruikt. \n" \
        "In een setup definieer je welke outboard gear je op welk kanaal van de mengtafel hebt gezet.\n" \
        "Eenmaal je setup is opgeslagen kan je aan de gang met ingeven welke settings je op je outboard gear hebt gebruikt.\n\n" \
        "Veel recall-plezier!")
        self.tekst_uitleg = Message(self, width=600, text=var_uitleg)
        self.tekst_uitleg.place(relx=0.2, rely=0.3)


