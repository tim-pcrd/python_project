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

    def select_all_projects(self):
        db = Db()
        query = "SELECT projectID, albumName, lastName, firstName \
                 FROM projects p \
                 JOIN users u \
                 ON p.artistID = u.userID"
        db_results = db.db_select(query)

        projects: list[ActiveProject] = []
        if db_results:
            for result in db_results:
                project = ActiveProject()
                project.projectID = result[0]
                project.album_name = result[1]
                project.last_name = result[2]
                project.first_name = result[3]
                projects.append(project)

        return projects

    def select_all_active_projects(self):
        db = Db()
        query = "SELECT projectID, albumName, lastName, firstName \
                 FROM projects p \
                 JOIN users u \
                 ON p.artistID = u.userID \
                 WHERE endDate IS NULL"
        db_results = db.db_select(query)

        projects: list[ActiveProject] = []
        if db_results:
            for result in db_results:
                project = ActiveProject()
                project.projectID = result[0]
                project.album_name = result[1]
                project.last_name = result[2]
                project.first_name = result[3]
                projects.append(project)

        return projects



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

    # retrieve all sessions from database
    def select_all_sessions(self):
        db = Db()
        query = "SELECT s.sessionID, sessiontypeName, setupName, setupDescription \
                 FROM sessions s JOIN sessiontypes st \
                 ON s.sessiontypeID = st.sessiontypeID \
                 JOIN setups stps \
                 ON s.setupID = stps.setupID"
        db_results = db.db_select(query)

        sessions: list[ActiveSession] = []
        if db_results:
            for result in db_results:
                session = ActiveSession()
                session.sessionID = result[0]
                session.session_type_name = result[1]
                session.setup_name = result[2]
                session.setup_description = result[3]
                sessions.append(session)

        return sessions
