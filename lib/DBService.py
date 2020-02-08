import sqlite3
import datetime

class DB(object):
    
    def __init__(self):
        self.conn = sqlite3.connect('db/data.sqlite3')
        self.c = self.conn.cursor()

    def checkExistNameZip(self, name_zip):

        self.c.execute('SELECT COUNT(*) FROM backup WHERE name_zip=?', (name_zip, ))    
        
        return self.c.fetchone()[0]

    def registerBackup(self, name_zip):

        result = True

        now = datetime.datetime.now().__str__()
        
        try:
            self.c.execute('INSERT INTO backup VALUES (null, ?, ?, ?)', (name_zip, now, 0))    
            self.conn.commit()          
        finally:
            result = False

        return result
        
    def setAsSentBackup(self, name_zip):

        result = True

        try:
            self.c.execute('UPDATE backup set isSent=1 where name_zip =?', (name_zip, ))    
            self.conn.commit()          
        finally:
            result = False

        return result

    def close():
        self.conn.close()