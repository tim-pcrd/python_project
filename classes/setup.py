from classes.db import Db


class ActiveProject:
    def __init__(self, projectID, name, artistID):
        self.projectID=projectID
        self.name=name
        self.artistID=artistID


class ActiveSession:
    def __init__(self):
        pass

class ActiveSetup:
    def __init__(self, setupID):
        self.setupID=setupID

    def get_gearlist(self):
        pass


class ActiveChain:
    def __init__(self):
        self.setupID = "1"
        self.sessionID = ""
        self.chainName

        self.pos1 = None
        self.pos2 = None
        self.pos3 = None
        self.pos4 = None
        self.pos5 = None

    #def select_chain(self):


    def select_chain(self, chainID):
        db = Db()
        query = 'SELECT chainName FROM chains WHERE chainID = %s '
        data = (chainID)
        result = db.db_select(query,data)

        if result and len(result) == 1:
            for chain in result:
                self.chainID = chain[0]
                self.chainName = chain[1]
                self.pos1 = None
                self.pos2 = None
                self.pos3 = None
                self.pos4 = None
                self.pos5 = None
