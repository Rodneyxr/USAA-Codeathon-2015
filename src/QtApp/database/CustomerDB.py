from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 
from QtApp.model.FlightClass import Flight

class CustomerDB:
   def authUser(username,password):
      db = Database.getDatabase()
      query = CustomerQuery(db)
      custID = query.authUser(username,password)
      return custID

   def getFlights(custID):
      db = Database.getDatabase()
      query = CustomerQuery(db)
      return query.getFlights(custID)

#function queries
class CustomerQuery(QSqlQuery):
   authUserQuery = "SELECT CustID FROM Customer WHERE UserName = :username AND PassHash = :passhash"
   getBFlightsQuery = """SELECT Flights.* FROM Customer
    LEFT JOIN BookedFlights ON Customer.CustID = BookedFlights.CustID
    LEFT JOIN Flights ON Flights.FlightID = BookedFlights.FlightID
    WHERE Customer.CustID = :custID"""

   def __init__(self,database):
      super().__init__(database)
     
   def authUser(self,username,passHash):
      self.prepare(self.authUserQuery)
      self.bindValue(":username",username)
      self.bindValue(":passHash",passHash)

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)
      
      rec = self.record()
      custID = -1
      if(self.next()):
         index = rec.indexOf('CustId')
         custID = self.value(index)

      return custID

   def getFlights(self,custID):
      self.prepare(self.getBFlightsQuery)
      self.bindValue(":custID",str(custID))

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
