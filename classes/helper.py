from tkinter import W, Label
import settings
import bcrypt

class Helper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def hash_password(password):
        hashed = bcrypt.hashpw(password.encode('utf-8') , bcrypt.gensalt())
        return hashed.decode('utf-8')

    @staticmethod
    def check_password(password, hashed_password):
        if bcrypt.checkpw(password.encode('utf-8') , hashed_password.encode('utf-8')):
            return True
        else: 
            return False

    @staticmethod
    def error_message(root, message):
        if root.message:
            root.message.destroy()
        root.message = Label(root, text=f"{message}", bg=settings.PROGRAM_BG, fg='red',font=("Arial", 12), anchor=W, padx=5, 
        highlightbackground="red", highlightcolor="red", highlightthickness=3)
        root.message.place(x=15, rely=0.910, height=40, width=400)

    @staticmethod
    def success_message(root, message):
        if root.message:
            root.message.destroy()
        root.message = Label(root, text=f"{message}", bg=settings.PROGRAM_BG, fg='green',font=("Arial", 12), anchor=W, padx=5,
            highlightbackground="green", highlightcolor="green", highlightthickness=3)
        root.message.place(x=15, rely=0.910, height=40, width=400)

    @staticmethod
    def clear_message(root):
        if root.message:
            root.message.destroy()
