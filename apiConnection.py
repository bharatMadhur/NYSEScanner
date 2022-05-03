# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:59:10 2022

@author: ycgao
"""

import requests
from datetime import datetime, timedelta



class apiConnection():
    def __init__(self):
        self.__url = "https://api.tiingo.com/tiingo/daily/"
        self.__headers = {
            'Content-Type': 'application/json'
        }
        self.__token = "2f7e85db1869a38072f3348bdae03512c8438e30"
        
    def request(self, stockName, date):
        requestResponse = requests.get(self.__url+stockName+"/prices?startDate="+date+"&token="+self.__token, headers = self.__headers)
        try:
            return requestResponse.json()
        except:
            return ""
     
today = datetime.today()
thirty_days_ago = today - timedelta(days=90)
print(type(thirty_days_ago))

#date_time = thirty_days_ago.strftime("%m-%d-%Y")
date_time = thirty_days_ago.strftime("%Y-%m-%d")
request=apiConnection()
request.request("AMZN", "1")