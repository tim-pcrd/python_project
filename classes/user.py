from classes.db import Db


class User:
    def __init__(self):
        self.logged_in = False

        self.userID = None
        self.roleId = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.manager = None
        self.stage_name = None
        self.password = None


    def create_user(self,email, password, firstName, lastName):
        db = Db()
        query = 'INSERT INTO users (emailAddress, password, firstName, lastName, roleID) VALUES (%s,%s,%s,%s,%s);'
        data = (email, password, firstName, lastName, 2)
        result = db.db_insert(query, data)

        return result

    
    def login_user(self, email, password):
        db = Db()
        query = 'SELECT * FROM users WHERE emailAddress = %s AND password = %s'
        data = (email, password)
        result = db.db_select(query,data)

        if result and len(result) == 1:
            for user in result:
                self.userID = user[0]
                self.roleId = user[1]
                self.first_name = user[3]
                self.last_name = user[2]
                self.email = user[4]
                self.password = user[5]
                self.stage_name = user[6]
                self.manager = user[7]


    def update_user(self, email, first_name, last_name):
        db = Db()
        query = "UPDATE users SET firstName = %s, lastName = %s, emailAddress = %s where userID = %s"
        data = (first_name, last_name, email, self.userID)
        result = db.db_update(query, data)

        if result:
            self.select_user(self.userID)
            return True

        return False


    def change_password(self, password):
        db = Db()
        query = "UPDATE users set password = %s where userID = %s"
        data = (password, self.userID)
        result =db.db_update(query, data)

        if result:
            self.select_user(self.userID)
            return True

        return False



    def select_user(self, id):
        db = Db()
        query = 'SELECT * FROM users WHERE userID = %s'
        data = (id,)
        result = db.db_select(query,data)

        if result and len(result) == 1:
            for user in result:
                self.userID = user[0]
                self.roleId = user[1]
                self.first_name = user[3]
                self.last_name = user[2]
                self.email = user[4]
                self.password = user[5]
                self.stage_name = user[6]
                self.manager = user[7]


    def __str__(self) -> str:
        return f'{self.userID}, {self.roleId}, {self.first_name}, {self.last_name}'
        