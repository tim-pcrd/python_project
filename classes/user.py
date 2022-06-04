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
        self.role = None


    def create_user(self,email, password, firstName, lastName):
        db = Db()
        query = 'INSERT INTO users (emailAddress, password, firstName, lastName, roleID) VALUES (%s,%s,%s,%s,%s);'
        data = (email, password, firstName, lastName, 1)
        result = db.db_insert(query, data)

        return result

    
    def login_user(self, email, password):
        db = Db()
        query = 'SELECT u.*, r.role FROM users u inner join roles r on r.roleID = u.roleID WHERE emailAddress = %s AND password = %s'
        data = (email, password)
        result = db.db_select_one(query,data)

        if result:
            self.userID = result[0]
            self.roleId = result[1]
            self.first_name = result[3]
            self.last_name = result[2]
            self.email = result[4]
            self.password = result[5]
            self.stage_name = result[6]
            self.manager = result[7]
            self.role = result[8]


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


    def check_email_exists(self, email):
        db = Db()
        query = "SELECT COUNT(*) FROM users where emailAddress = %s"
        data = (email,)
        result = db.db_select_one(query,data)

        if result and result[0] > 0 :
            return True

        return False


    def select_user(self, id):
        db = Db()
        query = 'SELECT u.*, r.role FROM users u inner join roles r on r.roleID = u.roleID WHERE userID = %s'
        data = (id,)
        result = db.db_select_one(query,data)

        if result:
            self.userID = result[0]
            self.roleId = result[1]
            self.first_name = result[3]
            self.last_name = result[2]
            self.email = result[4]
            self.password = result[5]
            self.stage_name = result[6]
            self.manager = result[7]
            self.role = result[8]

    def select_all_users(self, exludedId = 0):
        db = Db()
        query = "SELECT * FROM users where userID != %s"
        data = (exludedId,)
        db_results = db.db_select(query, data)

        users: list[User] = []
        if db_results:
            for result in db_results:
                user = User()
                user.userID = result[0]
                user.roleId = result[1]
                user.first_name = result[3]
                user.last_name = result[2]
                user.email = result[4]
                user.password = result[5]
                user.stage_name = result[6]
                user.manager = result[7]
                users.append(user)

        return users

    def select_all_musicians(self, roleId):
        db = Db()
        query = "SELECT * FROM users WHERE roleId = %s ORDER BY lastName"
        data = (roleId,)
        db_results = db.db_select(query, data)

        musicians: list[User] = []
        if db_results:
            for result in db_results:
                user = User()
                user.userID = result[0]
                user.roleId = result[1]
                user.first_name = result[3]
                user.last_name = result[2]
                user.email = result[4]
                user.password = result[5]
                user.stage_name = result[6]
                user.manager = result[7]
                musicians.append(user)

        return musicians


    def __str__(self) -> str:
        return f'{self.userID}, {self.roleId}, {self.first_name}, {self.last_name}'
        