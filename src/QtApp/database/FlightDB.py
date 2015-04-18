from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightsQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 

class UserDB:
   def getFlights():

   def retrieveUser(username):
      db = Database.getDatabase()
      query = CustomerQuery(db)
      resultDict = query.getUser(username)
      return resultDict

   def addUser(**kwargs):
      db = Database.getDatabase()
      transaction = db.transaction()
      if(not transaction):
         return False

      query = CustomerQuery(db)
      try:
         query.addUser(**kwargs)
      except Exception as e:
         db.rollback()
         raise e

      commited = db.commit()
      if(not commited):
         db.rollback()

      return commited

#function queries
class FlightQuery(QSqlQuery):
   getFlightQuery = "SELECT * FROM {0}".format(FQN.tableName)

   def __init__(self,database):
      super().__init__(database)
      
   def getFlights(self):
      self.prepare(self.getFlightQuery)

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

      rec = self.record()
      if(not self.next()):
         return None

      

   def getUser(self,username):
      self.prepare(self.getUserQuery)
      self.bindValue(QN.usernameTag,username)
      
      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

      rec = self.record()
      if(not self.next()):
         self.clear()
         raise NoSuchUser(username)

      resultDict = {}
      for field in QN.genFields():
         index = rec.indexOf(field)
         if(index == -1):
            continue

         value = query.value(index)
         if(type(value) is QPyNullVariant):
            value = ''

         resultDict[field] = value
      
      self.clear()
      return resultDict
