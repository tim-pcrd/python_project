from classes.db import Db




#--------------ACTIVE SETUP-----------------

class ActiveSetup:
    def __init__(self):
        self.setupID =          None
        self.setupName=         None
        self.setupDescription=  None

    def __str__(self) -> str:
        return f'ActiveSetup contains:\nID=\t\t{self.setupID}\nName=\t{self.setupName}\ndesc=\t{self.setupDescription}'


#haal een setup uit database en maak deze de actievesetup
    def load_setup(self, setupID):
        db=Db()
        query = "SELECT * FROM setups WHERE setupID=%s"
        data = [setupID]
        result = db.db_select_one(query,data)
        print(result)

        self.setupID = result[0]
        self.setupName = result[1]
        self.setupDescription = result[2]

#haalt alle setups op en zet in lijst
    def get_setuplist(self):
        setuplist = []
        db = Db()
        query = "SELECT setupID, setupName , setupDescription FROM setups;"
        data = ()
        result = db.db_select(query, data)
        for x in result:
            setuplist.append(x)
        return setuplist


#concerned haalt enkel de chains op die in de actieve setup zitten en zet in lijst
    def get_chainlist_concerned(self, setupID):
        chainlist_concerned = []
        db = Db()
        query = "SELECT setup_chain.chain_setupID, chains.chainID, chainName \
                        FROM chains \
                       JOIN setup_chain \
                        ON   chains.chainID=setup_chain.chainID \
                        WHERE setup_chain.setupID = %s ;"
        data = [setupID, ]
        result = db.db_select(query, data)
        for x in result:
            chainlist_concerned.append(x)
        return chainlist_concerned

#haalt alle chains op en zet ze in een lijst
    def get_chainlist(self):
        chainlist = []
        db = Db()
        query = "SELECT * FROM chains ORDER BY chainID ASC;"
        data = []
        result = db.db_select(query, data)
        for x in result:
            chainlist.append(x)
        return chainlist


#haalt een lijst op met alle gearunits
    def get_gearlist(self):
        gearlist=[]
        db=Db()
        query = "SELECT gearunitID, gearunitName FROM gearunits;"
        data =""
        result =db.db_select(query, data)
        for x in result:
            gearlist.append(x)
        return gearlist



#--------------ACTIVE CHAIN-----------------


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


#haalt een chain uit de database met zijn gekoppelde gearunits en zet de naam ervan in activechain
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



    def write_chain(self, setupID, chainID):
        db = Db()
        data=[setupID,chainID]
        query="INSERT INTO setup_chain (`setupID`, `chainID`) VALUES (%s , %s );"
        result = db.db_insert(query,data)
        return result


