from classes.db import Db







class ActiveSetup:
    def __init__(self, setupID):
        self.setupID=setupID
        self.setupName=""
        self.setupDescription=""

    def load_setup(self, setupID):
        db=Db()
        query = "SELECT * FROM setups; WHERE setupID=%s"
        data = setupID
        result = db.db_select(query,data)

        if result and len(result) == 1:
            for setup in result:
                self.setupID = setup[0]
                self.setupName = setup[1]
                self.setupDescription = setup[3]





    def get_gearlist(self):
        gearlist=[]
        db=Db()
        query = "SELECT gearunitID, gearunitName FROM gearunits;"
        data =""
        result =db.db_select(query, data)
        for x in result:
            gearlist.append(x)
        return gearlist


class ActiveChain:
    def __init__(self):
        self.chainID = "test"
        self.chainName = "Empty"

        self.pos1 = "None"
        self.pos2 = "None"
        self.pos3 = "None"
        self.pos4 = "None"
        self.pos5 = "None"

    #def select_chain(self):


    def select_chain(self, chainID):
        db = Db()
        query = """SELECT chains.chainID, chainName, unitPosition, gearunitName 
                    FROM chains 
                    CROSS JOIN chain_gearunit 
                    ON chains.chainID=chain_gearunit.chainID 
                    CROSS JOIN gearunits
                    ON chain_gearunit.gearunitID=gearunits.gearunitID
                    
                    WHERE chains.chainID = %s """
        data = [chainID]
        result = db.db_select(query, data)
        print(result)
        #if result and len(result) == 1:
        for chain in result:
            self.chainID = chain[0]
            self.chainName = chain[1]
            if chain[2] == 1:
                self.pos1 = chain[3]
            if chain[2] == 2:
                self.pos2 = chain[3]
            if chain[2] == 3:
                self.pos3 = chain[3]
            if chain[2] == 4:
                self.pos4 = chain[3]
            if chain[2] == 5:
                self.pos5 = chain[3]

    def __str__(self) -> str:
        return f'ActiveChain contains: {self.chainID}, {self.chainName}, {self.pos1}, {self.pos2}, {self.pos3}, {self.pos4}, {self.pos5}'

ActiveChain.select_chain(ActiveChain,2)
print(ActiveChain())