# from QtApp.database.PaymentDB import PaymentDB as PDB
#
#
# class PaymentInfo:
#     # PaymentID, CustomerID, FlightID, Merchant, Price, CardNum, ExpDate, Zip, CSV
#     def __init__(self, **kwargs):
#         self.paymentID = kwargs[PDB.paymentIDField]
#         self.customerID = kwargs[PDB.customerIDField]
#         self.flightID = kwargs[PDB.flightIDField]
#         self.merchant = kwargs[PDB.merchantField]
#         self.price = kwargs[PDB.priceField]
#         self.cardNum = kwargs[PDB.cardNumField]
#         self.expDate = kwargs[PDB.expDateField]
#         self.zip = kwargs[PDB.zipField]
#         self.csv = kwargs[PDB.csvField]
#
#     # Return PaymentID
#     def getPaymentID(self):
#         return self.paymentID
#
#     #Return CustomerID
#     def getCustomerID(self):
#         return self.customerID
#
#     #Return FlightID
#     def getFlightID(self):
#         return self.flightID
#
#     #Return Merchant
#     def getMerchant(self):
#         return self.merchant
#
#     #Return Price
#     def getPrice(self):
#         return self.price
#
#     #Return CardNum
#     def getCardNum(self):
#         return self.cardNum
#
#     #Return ExpDate
#     def getExpDate(self):
#         return self.expDate
#
#     #Return Zip
#     def getZip(self):
#         return self.zip
#
#     #Return CSV
#     def getCSV(self):
#         return self.csv
#
#     #Setting PaymentID
#     def setPaymentID(self, paymentID):
#         self.paymentID = paymentID
#
#     #Setting CustomerID
#     def setCustomerID(self, customerID):
#         self.customerID = customerID
#
#     #Setting FlightID
#     def setFlightID(self, flightID):
#         self.flightID = flightID
#
#     #Setting Merchant
#     def setMerchant(self, merhcant):
#         self.merchant = merhcant
#
#     #Setting Price
#     def setPrice(self, price):
#         self.price = price
#
#     #Setting CardNum
#     def setCardNum(self, cardNum):
#         self.cardNum = cardNum
#
#     #Setting ExpDate
#     def setExpDate(self, expDate):
#         self.expDate = expDate
#
#     #Setting Zip
#     def setZip(self, zip):
#         self.zip = zip
#
#     #Setting CSV
#     def setCSV(self, csv):
#         self.csv = csv