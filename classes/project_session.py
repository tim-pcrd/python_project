from classes.db import Db


#-----PROJECT CLASS----------------


class ActiveProject:
    def __init__(self):
        self.projectID = None
        self.albumName = None
        self.artistID = None
        self.startDate = None
        self.endDate = None

    def load_project(self, projectID):
        db = Db()
        query = "SELECT * FROM projects; WHERE projectID=%s"
        data = projectID
        result = db.db_select(query, data)

        self.projectID =    result[0]
        self.albumName =    result[1]
        self.artistID =     result[3]
        self.startDate =    result[2]
        self.endDate =      result[4]

    def select_project(self, id):
        db = Db()
        query = 'SELECT p.projectID, p.albumName, u.lastName, u.firstName, p.startDate, p.endDate \
                 FROM projects p \
                 JOIN users u \
                 ON p.artistID = u.userID \
                 WHERE p.projectID = %s'
        data = (id,)
        result = db.db_select_one(query, data)

        if result:
            project = ActiveProject()
            project.projectID = result[0]
            project.album_name = result[1]
            project.last_name = result[2]
            project.first_name = result[3]
            project.start_date = result[4]
            project.end_date = result[5]

        return project

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

    def add_project(self, albumName, artistID):
        db = Db()
        query = "INSERT INTO projects(albumName, artistID, startDate) VALUES (%s, %s, NOW());"
        data = (albumName, artistID)
        result = db.db_insert(query, data)

        return result

    def rename_project(self, albumName, projectID):
        db = Db()
        query = "UPDATE projects SET albumName = %s WHERE projectID = %s"
        data = (albumName, projectID)
        result = db.db_update(query, data)

        if result:
            return result

        return False

    def finalize_project(self, projectID):
        db = Db()
        query = "UPDATE projects SET endDate = NOW() WHERE projectID = %s"
        data = (projectID,)
        result = db.db_update(query, data)

        if result:
            return result

        return False

    def check_project_exists(self, name):
        db = Db()
        query = "SELECT COUNT(*) FROM projects WHERE albumName = %s"
        data = (name,)
        result = db.db_select_one(query, data)

        if result and result[0] > 0 :
            return True

        return False




#-----SESSION CLASS----------------


class ActiveSession:
    def __init__(self):
        self.sessionID =        None
        self.sessionName=       None
        self.projectID =        None
        self.setupID =          None
        self.date =             None
        self.sessiontypeID =    None


    def __str__(self) -> str:
        return f'ActiveSession contains:\nsessionID=\t\t{self.sessionID}\nsession name=\t{self.sessionName}\nprojectID=\t\t{self.projectID}\nsetupID=\t\t{self.setupID}\ndate=\t\t\t{self.date}\nsessiontypeID=\t{self.sessiontypeID}'


    def load_session(self, sessionID):
        db = Db()
        query = "SELECT * FROM sessions  WHERE sessionID=%s; "
        data = (sessionID)
        result = db.db_select_one(query, data)

        if result:
            self.sessionID =        result[0]
            self.sessionName=       result[1]
            self.projectID =        result[2]
            self.setupID =          result[3]
            self.date =             result[4]
            self.sessiontypeID =    result[5]


    def load_newest_session(self):
        db = Db()
        query = "SELECT * FROM sessions  WHERE id=(SELECT max(id) FROM sessions);"
        data = ()
        result = db.db_select_one(query, data)

        if result:
            self.sessionID =        result[0]
            self.projectID =        result[1]
            self.setupID =          result[2]
            self.date =             result[3]
            self.sessiontypeID =    result[4]


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
            # self.sessionID =        result[0]
            # self.projectID =        result[1]
            # self.setupID =          result[2]
            # self.date =             result[3]
            # self.sessiontypeID =    result[4]


    def select_project_sessions(self, id):
        db = Db()
        query = "SELECT sessions.sessionID, sessions.sessionName, projects.albumName, \
                 sessiontypes.sessiontypeName, setups.setupName, \
                 setups.setupDescription \
                 FROM projects \
                 JOIN sessions \
                 ON projects.projectID = sessions.projectID \
                 JOIN sessiontypes \
                 ON sessiontypes.sessiontypeID = sessions.sessiontypeID \
                 JOIN setups \
                 ON setups.setupID = sessions.setupID \
                 WHERE projects.projectID = %s"
        data = (id,)
        db_results = db.db_select(query, data)

        sessions: list[ActiveSession] = []
        if db_results:
            for result in db_results:
                session = ActiveSession()
                session.sessionID = result[0]
                session.session_name = result[1]
                session.album_name = result[2]
                session.session_type_name = result[3]
                session.setup_name = result[4]
                session.setup_description = result[5]
                sessions.append(session)

        return sessions

    def add_session(self, sessionName, projectID, setupID):
        db = Db()
        query = "INSERT INTO sessions (sessionName, projectID, setupID, date) VALUES (%s, %s, %s, NOW());"
        data = (sessionName, projectID, setupID)
        result = db.db_insert(query, data)

        return result