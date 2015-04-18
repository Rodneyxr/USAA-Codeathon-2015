from QtApp.database.FlightsTable import FlightQueryNames as FQN
import datetime


class Flight:
    # FlightID,FlightOrigin,FlightDestination, Departure, Arrival,UnoccupiedSeats
    def __init__(self, **kwargs):
        self.data = list()
        self.data.append(kwargs[FQN.flightIDField])  # 0
        self.data.append(kwargs[FQN.originField])  # 1
        self.data.append(kwargs[FQN.destField])  # 2
        self.data.append(kwargs[FQN.departTimeField])  # 3
        self.data.append(kwargs[FQN.arriveTimeField])  # 4
        self.data.append(kwargs[FQN.availSeatsField])  # 5

    # Return FlightID
    def getFlightID(self):
        return self.data[0]

        # Setting FlightID

    def setFlightID(self, flightID):
        self.data[0] = flightID

    # Return FlightOrigin
    def getFlightOrigin(self):
        return self.data[1]

    # Setting FlightOrigin
    def setFlightOrigin(self, flightOrigin):
        self.data[1] = flightOrigin

    # Return FlightDestination
    def getFlightDestination(self):
        return self.data[2]

    # Setting FlightDestination
    def setFlightDestination(self, flightDestination):
        self.data[2] = flightDestination

    # Return Departure time
    def getDeparture(self):
        return self.data[3]

    # Setting Departure time
    def setDeparture(self, departure):
        self.data[3] = departure

    # Return Arrival time
    def getArrival(self):
        return self.data[4]

    # Setting Arrival time
    def setArrival(self, arrival):
        self.data[4] = arrival

    # Return UnoccupiedSeats
    def getUnoccupiedSeats(self):
        return self.data[5]

    # Setting UnoccupiedSeats
    def setUnoccupiedSeats(self, unoccupiedSeats):
        self.data[5] = unoccupiedSeats

    def __len__(self):
        return len(self.data)