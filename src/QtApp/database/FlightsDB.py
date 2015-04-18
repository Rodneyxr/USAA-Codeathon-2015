from PyQt4.QtSql import QSqlQuery,QSqlDriver
from PyQt4.QtCore import QPyNullVariant
from QtApp.database.Database import Database
from QtApp.database.FlightsTable import FlightQueryNames as FQN
from QtApp.database.FlightsTable import QueryError 
from QtApp.model.FlightClass import Flight

class FlightsDB:
   """Gateway to flights table in qtpi database"""

   def bookFlight(flightID):
      db = Database.getDatabase()
      db.transaction()
      query = FlightQuery(db)
      query.bookFlight(flightID)
      db.commit()

   def killFlight(flightID):
      db = Database.getDatabase()
      db.transaction()
      query = FlightQuery(db)
      query.killFlight(flightID)
      db.commit()

   def getFlights():
      db = Database.getDatabase()
      query = FlightQuery(db)
      return query.getFlights()
   
   def searchFlightsArrival(arrival):
      db = Database.getDatabase()
      query = FlightQuery(db)
      return query.searchFlightsArrival(arrival)
   
   def searchFlightsDeparture(departure):
      db = Database.getDatabase()
      query = FlightQuery(db)
      return query.searchFlightsDeparture(departure) 
   
   def searchFlightsArrivalDeparture(arrival,departure):
      db = Database.getDatabase()
      query = FlightQuery(db)
      return query.searchFlightsArrivalDeparture(arrival,departure) 

class FlightQuery(QSqlQuery):
   getFlightQuery = "SELECT * FROM {0}".format(FQN.tableName)
   bookFlightQuery = "INSERT INTO BookedFlights (CustID,FlightID) VALUES ({0},{1})"
   decFlightQuery = "UPDATE Flights SET UnoccupiedSeats = UnoccupiedSeats - 1 WHERE FlightID = {0}"
   killFlightQuery = "DELETE FROM  BookedFlights WHERE CustID = {0} AND FlightID = {1}"
   incFlightQuery = "UPDATE Flights SET UnoccupiedSeats = UnoccupiedSeats + 1 WHERE FlightID = {0}"

   def __init__(self,database):
      super().__init__(database)

   def __decFlightSeats__(self,flightID):
      query = self.decFlightQuery.format(':flightID')

      self.prepare(query)
      self.bindValue(':flightID',str(flightID))

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

   def __incFlightSeats__(self,flightID):
      query = self.incFlightQuery.format(':flightID')

      self.prepare(query)
      self.bindValue(':flightID',str(flightID))

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

   def bookFlight(self,flightID):
      query = self.bookFlightQuery.format(':custID',':flightID')
      
      self.prepare(query)
      self.bindValue(':custID','1')
      self.bindValue(':flightID',str(flightID))

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

      self.__decFlightSeats__(flightID)

   def killFlight(self,flightID):
      query = self.killFlightQuery.format(':custID',':flightID')
      
      self.prepare(query)
      self.bindValue(':custID','1')
      self.bindValue(':flightID',str(flightID))

      succeeded = self.exec_()
      if(not succeeded):
         lastError = self.lastError().text()
         raise QueryError(lastError)

      self.__incFlightSeats__(flightID)

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

   def searchFlightsArrival(self,arrival):
      query = self.getFlightQuery
      date = arrival.toString(1)
      query += " WHERE DATE({0}) = {1}".format(FQN.arriveTimeField,FQN.arriveDateTag)

      self.prepare(query)
      self.bindValue(FQN.arriveDateTag,date)

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
   
   def searchFlightsDeparture(self,departure):
      query = self.getFlightQuery
      date = departure.toString(1)
      query += " WHERE DATE({0}) = {1}".format(FQN.departTimeField,FQN.departDateTag)
      
      self.prepare(query)
      self.bindValue(FQN.departDateTag,date)

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
   
   def searchFlightsArrivalDeparture(self,arrival,departure):
      query = "{0} WHERE DATE({1}) = {2} AND DATE({3}) = {4}".format(
              self.getFlightQuery,
              FQN.arriveTimeField,
              FQN.arriveDateTag,
              FQN.departTimeField,
              FQN.departDateTag
            )

      aDate = arrival.toString(1)
      dDate = departure.toString(1)

      self.prepare(query)
      self.bindValue(FQN.arriveDateTag,aDate)
      self.bindValue(FQN.departDateTag,dDate)

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
