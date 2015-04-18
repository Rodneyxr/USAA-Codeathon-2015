# A module containing names pertaining
# to the 'Customer' table of the mysql
# database 'qtpi'. As well as some
# query-related exceptions

class FlightQueryNames:
   #database name
   dbName = "qtpi"

   #table name
   tableName = "Flights"

   #column names in flights table
   flightIDField = "FlightID"
   originField = "FlightOrigin"
   destField = "FlightDestination"
   departTimeField = "Departure"
   arriveTimeField = "Arrival"
   availSeatsField = "UnoccupiedSeats"

   #tags for prepared queries
   flightIDTag = ":flightID"
   originTag = ":origin"
   destTag = ":destination"
   departTimeTag = ":departure" 
   arriveTimeTag = ":arrival"
   availSeatsTag = ":seats"

   #generates database field strings
   #outputs in same order as genTags      
   def genFields():
      QN = FieldQueryNames
      yield QN.flightIDField
      yield QN.originField
      yield QN.destField
      yield QN.departTimeField
      yield QN.arriveTimeField
      yield QN.availSeatsField

   #generates database tag strings
   #outputs in same order as genFields
   def genTags():
      QN = FieldQueryNames
      yield QN.flightIDTag
      yield QN.originTag
      yield QN.destTag
      yield QN.departTimeTag
      yield QN.arriveTimeTag
      yield QN.availSeatsTag
   
   def genFieldsTagsZip():
      QN = FieldQueryNames
      yield (QN.flightIDField,QN.flightIDTag)$
      yield (QN.originField,QN.originTag)$
      yield (QN.destField,QN.destTag)$
      yield (QN.departTimeField,QN.departTimeTag)$
      yield (QN.arriveTimeField,QN.arriveTimeTag)$
      yield (QN.availSeatsField,QN.availSeatsTag)$


class QueryError(Exception):
   def __init__(self,lastError):
      self.lastError = lastError

   def __str__(self):
      errMessage = "Query Error: {0}".format(self.lastError)
      return self.lastError
