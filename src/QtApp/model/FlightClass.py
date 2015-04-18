from QtApp.database.FlightsTable import FlightQueryNames as FQN

class Flights:
   #FlightID,FlightOrigin,FlightDestination, Departure, Arrival,UnoccupiedSeats
   def __init__(self,**kwargs):
      self.flightID = kwargs[FQN.flightIDField]
      self.flightOrigin = kwargs[FQN.originField]
      self.flightDestination = kwargs[FQN.destinationField]
      self.departure = kwargs[FQN.departTimeField]
      self.arrival = kwargs[FQN.arriveTimeField]
      self.unoccupiedSeats= kwargs[FQN.availSeatsField]

    #Return FlightID
   def getFlightID(self):
      return self.flightID

    #Return FlightOrigin
   def getFlightOrigin(self):
      return self.flightOrigin

    #Return FlightDestination
   def getFlightDestination(self):
      return self.flightDestination

    #Return Departure time
   def getDeparture(self):
      return self.departure

    #Return Arrival time
   def getArrival(self):
      return self.arrival

    #Return UnoccupiedSeats  
   def getUnoccupiedSeats(self):
      return self.unoccupiedSeats

    #Setting FlightID
   def setFlightID(self,flightID):
      self.flightID = flightID

    #Setting FlightOrigin
   def setFlightOrigin(self,flightOrigin):
      self.flightOrigin = flightOrigin
  
    #Setting FlightDestination  
   def setFlightDestination(self,flightDestination):
      self.flightDestination = flightDestination
  
    #Setting Departure time
   def setDeparture(self,departure):
      self.departure = departure
    
    #Setting Arrival time     
   def setArrival(self,arrival):
      self.arrival = arrival
    
    #Setting UnoccupiedSeats
   def setUnoccupiedSeats(self,unoccupiedSeats):
      self.unoccupiedSeats = unoccupiedSeats