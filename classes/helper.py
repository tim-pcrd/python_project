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
