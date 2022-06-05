from classes.db import Db


class Role:
    def __init__(self) -> None:
        self.roleID = None
        self.role = None

    @staticmethod
    def get_all_roles():
        db = Db()
        query = "SELECT * FROM roles"
        db_results = db.db_select(query)

        roles: list[Role] = []
        if db_results:
            for result in db_results:
                role = Role()
                role.roleID = result[0]
                role.role = result[1]
                roles.append(role)

        return roles


    def __str__(self) -> str:
        return f'{self.roleID}, {self.role}' 


        