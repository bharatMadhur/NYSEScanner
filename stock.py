import numpy as np
from apiConnection import apiConnection
from datetime import datetime, timedelta
from AnalysisFactory import *

class stock():
    def __init__(self, stockCode):
        self.__stockCode = ""
        # set date, auto set is 252
        today = datetime.today()
        early_days = today - timedelta(days=252)
        self.__date = early_days.strftime("%Y-%m-%d")
        
        self.__apiCon = apiConnection() #api connection
        self.__datas = self.__dataRequest(stockCode, self.__date)
        #extract stock data from json
        self.__close = []
        self.__high = []
        self.__low = []
        self.__open_price = []
        self.__volume = []
        self.__dataExtract()
    #stock request from api  
    def __dataRequest(self, stockCode, date):
        data = self.__apiCon.request(stockCode, date)
        return data
    
    #extract stock price information
    def __dataExtract(self):
        for data in self.__datas:
            self.__open_price.append(data['open'])
            self.__close.append(data['close'])
            self.__high.append(data['high'])
            self.__low.append(data['low'])
            self.__volume.append(data['volume'])
        self.__open_price = np.asarray(self.__open_price)
        self.__close = np.asarray(self.__close)
        self.__high = np.asarray(self.__high)
        self.__low = np.asarray(self.__low)
        self.__volume = np.asarray(self.__volume)
        
    def setStockCode(self, stockCode):
        self.__stockCode = stockCode
        
    def getStockCode(self):
        return self.__stockCode
    
    #get the how many days of data
    def setdate(self, days):
        today = datetime.today()
        early_days = today - timedelta(days)
        self.__date = early_days.strftime("%Y-%m-%d")
        
    def getdate(self):
        return self.__date
    
    def reloadData(self):
        self.__datas = self.__dataRequest(self.__stockCode, self.__date)
        self.__dataExtract()
        
    def analysis(self, analysisType):
        factory = AnalysisFactory()
        ## type  Recommendation Analysis, risk analysis, Sentiment analysis, Fundenmential analysis, Technical analysis
        analyst = factory.getAnalyst("Fundenmential analysis")
        analyst.getMetrix(self.__high, self.__low, self.__close)
        analyst.getAnalysis()
        
    
        
AMZN = stock("AMZN")
AMZN.analysis("Fundenmential analysis")


    