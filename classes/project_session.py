from classes.db import Db


class ActiveProject:
    def __init__(self):
        self.projectID= None
        self.albumName= None
        self.artistID= None
        self.startDate = None
        self.endDate = None

    def load_project(self, projectID):
        db=Db()
        query = "SELECT * FROM projects; WHERE projectID=%s"
        data = projectID
        result = db.db_select(query,data)

        if result and len(result) == 1:
            for project in result:
                self.projectID = project[0]
                self.albumName = project[1]
                self.artistID = project[3]
                self.startDate = project[2]
                self.endDate = project[4]



class ActiveSession:
    def __init__(self):
        self.sessionID= None
        self.projectID = None
        self.setupID = None
        self.date = None
        self.sessiontypeID = None

    def load_session(self, sessionID):
        db=Db()
        query = "SELECT * FROM session; WHERE sessionID=%s"
        data = sessionID
        result = db.db_select_one(query,data)

        if result:
            self.sessionID = result[0]
            self.projectID = result[1]
            self.setupID = result[2]
            self.date = result[3]
            self.sessiontypeID = result[4]