from PyQt4.QtSql import QSqlDatabase

#Creates a singleton database object
class Database:
   qtpiDB = None
   hostName = "localhost"
   port = 3306
   dbName = "qtpi"
   username = "root"
   password = "raspberry"
   dbType = "QMYSQL"
   connection = "connection1"

   def getDatabase():
      DB = Database
      if(DB.qtpiDB is not None):
         return DB.qtpiDB

      DB.qtpiDB = QSqlDatabase.addDatabase(DB.dbType,DB.connection)
      DB.qtpiDB.setHostName(DB.hostName)
      DB.qtpiDB.setPort(DB.port)
      DB.qtpiDB.setDatabaseName(DB.dbName)
      DB.qtpiDB.setUserName(DB.username)
      DB.qtpiDB.setPassword(DB.password)

      if(not DB.qtpiDB.open()):
         lastError = DB.qtpiDB.lastError().text()
         DB.qtpiDB = None
         raise FailedConnection(lastError)

      return DB.qtpiDB

   def endConnection():
      DB = Database
      DB.qtpiDB.close()
      DB.qtpiDB = None
      QSqlDatabase.removeDatabase(DB.connection)


class FailedConnection(Exception):
   def __init__(self,lastError):
      self.lastError = lastError

   def __str__(self):
      return self.lastError
