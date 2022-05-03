# -*- coding: utf-8 -*-
"""
Created on Tue May  3 07:55:00 2022

@author: ycgao
"""

from apiConnection import *

# apifactory = apiConnectionFactory()
# apiCon = apifactory.getConnection("Company information") #api connection
# apiCon.request("AMZN")
class forexInformation():
    def getInformation(self):
        apifactory = apiConnectionFactory()
        apiCon = apifactory.getConnection("forex") #api connection
        return apiCon.request()
    
forex = forexInformation()
print(forex.getInformation())