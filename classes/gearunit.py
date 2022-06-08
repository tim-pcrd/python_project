from classes.db import Db

class Gearunit:
    def __init__(self):
        self.gearunitID = None
        self.gearunit_name = None
        self.gearunit_type_id = None

    def __str__(self) -> str:
        return f'{self.gearunitID}, {self.gearunit_name}'

