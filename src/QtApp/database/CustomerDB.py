from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 
from QtApp.model.FlightClass import Flight

class CustomerDB:
   def getFlights():
      db = Database.getDatabase()
      query = CustomerQuery(db)
      return query.getFlights()

#function queries
class CustomerQuery(QSqlQuery):
   getBFlightsQuery = """SELECT Flights.* FROM Customer
    LEFT JOIN BookedFlights ON Customer.CustID = BookedFlights.CustID
    LEFT JOIN Flights ON Flights.FlightID = BookedFlights.FlightID
    WHERE Customer.CustID = 1"""

   def __init__(self,database):
      super().__init__(database)
     
   def getFlights(self):
      self.prepare(self.getBFlightsQuery)

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
