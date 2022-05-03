# -*- coding: utf-8 -*-
"""
Created on Tue May  3 07:55:00 2022

@author: ycgao
"""

from apiConnection import *

# apifactory = apiConnectionFactory()
# apiCon = apifactory.getConnection("Company information") #api connection
# apiCon.request("AMZN")
class companyInformation():
    def getInformation(self, stockName):
        apifactory = apiConnectionFactory()
        apiCon = apifactory.getConnection("Company information") #api connection
        return apiCon.request(stockName)
    
companyInf = companyInformation()
print(companyInf.getInformation("aapl"))