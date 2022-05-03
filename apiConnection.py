# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:59:10 2022

@author: ycgao
"""

import requests
from datetime import datetime, timedelta




     
# today = datetime.today()
# thirty_days_ago = today - timedelta(days=90)
# print(type(thirty_days_ago))

# #date_time = thirty_days_ago.strftime("%m-%d-%Y")
# date_time = thirty_days_ago.strftime("%Y-%m-%d")
# request=apiConnection()
# request.request("AMZN", "1")
class apiConnectionFactory:
    def getConnection(self, ConnectionType):
        if ConnectionType==None:
            return None
        if ConnectionType=="Stock data":
            return api_StockData()
        elif ConnectionType=="Company information":
            return api_aboutTheCompany()
        elif ConnectionType=="forex":
            return api_forex()
        elif ConnectionType=="currentPrice":
            return api_currentPrice()
        elif ConnectionType=="intradayChartingPrices":
            return api_intradayChartingPrices()
        elif ConnectionType=="fundamentalDow30":
            return api_fundamentalDow30()
        return None

from abc import ABC, abstractmethod
class apiConnection(ABC):
    def load(self):
        self._url = "https://api.tiingo.com/"
        self._headers = {
            'Content-Type': 'application/json'
        }
        self._token = "2f7e85db1869a38072f3348bdae03512c8438e30"
        
    @abstractmethod
    def request(self):
        pass
 
#stock market data       
class api_StockData(apiConnection):
    def request(self, stockName, date):
        s="tiingo/daily/"
        self.load()
        requestResponse = requests.get(self._url+s+stockName+"/prices?startDate="+date+"&token="+self._token, headers = self._headers)
        try:
            return requestResponse.json()
        except:
            return ""
    
# META ENDPOINT ABOUT THE COMPANY 
class api_aboutTheCompany(apiConnection):
    def request(self, stockName):
        s="tiingo/daily/"
        self.load()
        requestResponse = requests.get(self._url+s+stockName+"?token="+self._token)
        try:
            return requestResponse.json()
        except:
            return ""

class api_forex(apiConnection):
    def request(self):
        s="tiingo/fx/top?tickers=usdinr"
        self.load()
        requestResponse = requests.get(self._url+s+"&token="+self._token)
        try:
            return requestResponse.json()
        except:
            return ""
class api_currentPrice(apiConnection):
    def request(self, stockName):
        s="iex/？tickers="
        self.load()
        requestResponse = requests.get(self._url+s+stockName+"&token="+self._token)
        try:
            return requestResponse.json()
        except:
            return ""
        
class api_intradayChartingPrices(apiConnection):
    def request(self, startDate, stockName, freq):
        s="iex/"
        f="/prices?startDate=2022-04-26&resampleFreq=1hour&columns=open,high,low,close,volume"
        self.load()
        requestResponse = requests.get(self._url+s+stockName+f+"&token="+self._token)
        try:
            return requestResponse.json()
        except:
            return ""

class api_fundamentalDow30(apiConnection):
    def request(self, stockName):
        s="/tiingo/fundamentals/"
        f="/daily?startDate=2022-04-29"
        self.load()
        requestResponse = requests.get(self._url+s+stockName+f+"&token="+self._token)
        try:
            return requestResponse.json()
        except:
            return ""

# a=api_fundamentalDow30()
# a.request("aapl")