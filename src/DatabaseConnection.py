import sqlite3
from threading import RLock  

class DatabaseConnection:
    _instance = None
    # lock
    _lock = RLock()
    def __new__(cls, db_path='./database/budget_db.db'):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    #ADD check_same_thread=False HERE
                    cls._instance.conn = sqlite3.connect(db_path , check_same_thread=False)
                    cls._instance.conn.row_factory = sqlite3.Row
        return cls._instance
    

    def execute(self, query, params=()):
        """Execute a query"""
        with self._lock:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            return cursor
    
    def fetchone(self, query, params=()):
        """Execute and return one result"""
        cursor = self.execute(query, params)
        return cursor.fetchone()
    
    def fetchall(self, query, params=()):
        """Execute and return all results"""
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def commit(self):
        """Commit the current transaction"""
        with self._lock:
            self.conn.commit()
    
    def close(self):
        """Close the database connection"""
        with self._lock:
            if self.conn:
                self.conn.close()
                DatabaseConnection._instance = None