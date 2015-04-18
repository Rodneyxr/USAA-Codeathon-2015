from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 
from QtApp.model.FlightClass import Flight

class FlightsDB:
   """Gateway to flights table in qtpi database"""

   def getFlights():
      db = Database.getDatabase()
      query = FlightQuery(db)
      return query.getFlights()

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

      flights = []
      rec = self.record()
      while(self.next()):
         resultDict = {}
         for field in FQN.genFields():
            index = rec.indexOf(field)
            resultDict[field] = self.value(index)

         flights.append(Flight(**resultDict))
      
      return flights
