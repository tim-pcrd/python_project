import mysql.connector
from mysql.connector import (connection)


class Db:
    def __init__(self) -> None:
       self.db = None


    def db_select(self, query, data = None) -> list[tuple]:
        try:
            self.get_connection()

            db_cursor = self.db.cursor(buffered=True)
            if data:
                db_cursor.execute(query, data)
            else:
                db_cursor.execute(query)
            self.db.commit()

            result = db_cursor.fetchall()

            #return lijst van tuples
            return result
        
        except mysql.connector.Error as error:
            print(f'Select failed: {error}')
            return None

        finally:
            if self.db.is_connected():
                db_cursor.close()
                self.db.close()




    def db_insert(self, query: str, data) -> int:
        try:
            self.get_connection()

            db_cursor = self.db.cursor(buffered=True)
            db_cursor.execute(query,data)
            self.db.commit()

            #return primary key van nieuwe rij
            return db_cursor.lastrowid

        except mysql.connector.Error as error:
            print(f'Insert failed: {error}')

            # return 0 bij mislukte insert
            return 0;

        finally:
            if self.db.is_connected():
                db_cursor.close()
                self.db.close()


    def db_update(self, query: str, data) -> tuple:
        pass
        

    def db_delete(self, query: str) -> bool:
        try:
            self.get_connection()

            db_cursor = self.db.cursor(buffered=True)
            db_cursor.execute(query)
            self.db.commit()

            #return True (geslaagd) of False  
            return db_cursor.rowcount > 0

        except mysql.connector.Error as error:
            print(f'Delete failed: {error}')

            return False;
        
        finally:
            db_cursor.close()
            self.db.close()

    

    def get_connection(self):
        self.db = connection.MySQLConnection(
            user='sql11491613', 
            password='eWFcPv5Ndt',
            host='35.157.16.43',
            database='sql11491613')


