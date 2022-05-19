class User:
    def __init__(self):
        self.logged_in = False

        self.userID = None
        self.roleId = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.roleId = None
        self.manager = None
        self.stage_name = None
        self.password = None

    def __str__(self) -> str:
        return f'{self.userID}, {self.roleId}, {self.first_name}, {self.last_name}'
        