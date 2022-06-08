from classes.db import Db



class ActiveSetup:
    def __init__(self):
        self.setupID =          None
        self.setupName=         None
        self.setupDescription=  None

    def __str__(self) -> str:
        return f'ActiveSetup contains:\nID=\t\t{self.setupID}\nName=\t{self.setupName}\ndesc=\t{self.setupDescription}'



    def load_setup(self, setupID):
        db=Db()
        query = "SELECT * FROM setups WHERE setupID=%s"
        data = [setupID]
        result = db.db_select_one(query,data)
        print(result)

        self.setupID = result[0]
        self.setupName = result[1]
        self.setupDescription = result[2]


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
        self.chainID =  None
        self.chainName =None

        self.pos1 =     None
        self.pos2 =     None
        self.pos3 =     None
        self.pos4 =     None
        self.pos5 =     None

    def __str__(self) -> str:
        return f'ActiveChain contains:\nID=\t{self.chainID} \nName=\t{self.chainName} \n1=\t{self.pos1} \n2=\t{self.pos2} \n3=\t{self.pos3} \n4=\t{self.pos4} \n5=\t{self.pos5}'



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
        #print(result)
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


# ActiveChain.select_chain(ActiveChain,2)
# print(ActiveChain())

#ac=ActiveChain()
#ac.select_chain(1)
#print(ac)
