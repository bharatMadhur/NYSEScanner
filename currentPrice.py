# -*- coding: utf-8 -*-
"""
Created on Tue May  3 08:40:14 2022

@author: ycgao
"""

from apiConnection import *

# apifactory = apiConnectionFactory()
# apiCon = apifactory.getConnection("Company information") #api connection
# apiCon.request("AMZN")
class currentPriceInformation():
    def getInformation(self, stockName):
        apifactory = apiConnectionFactory()
        apiCon = apifactory.getConnection("currentPrice") #api connection
        return apiCon.request(stockName)
    
currentPrice = currentPriceInformation()
print(currentPrice.getInformation("aapl"))