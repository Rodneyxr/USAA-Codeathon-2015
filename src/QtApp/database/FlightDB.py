from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightsQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 
from QtApp.model.FlightClass import FlightsClass

class UserDB:
   def getFlights():
      db = Database.getDatabase()

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
      flights = []
      while(self.next()):
         resultDict = {}
         for field in FQN.genFields():
            index = rec.indexOf(field)
            resultDict[field] = self.value(index)
            flights.append(Flights(**resultDict))
      
      return flights
