# -*- coding: utf-8 -*-
"""
Created on Tue May  3 02:35:04 2022

@author: ycgao
"""

from metrix import Metrix
import numpy as np
from scipy import stats
import pandas as pd
from scipy.stats import norm

class AnalysisFactory:
    def getAnalyst(self, AnalystType):
        if AnalystType==None:
            return None
        if AnalystType=="Recommendation analysis":
            return RecommendationAnalysis()
        elif AnalystType=="risk analysis":
            return riskAnalysis()
        elif AnalystType=="Sentiment analysis":
            return sentimentalAnalysis()
        elif AnalystType=="Fundenmential analysis":
            return fundenmentialAnalysis()
        elif AnalystType=="Technical analysis":
            return technicalAnalysis()
        return None
    
from abc import ABC, abstractmethod
class analysis(ABC):
    def __int__(self):
        self._metrix = {}
        
    @abstractmethod
    def getAnalysis(self):
        pass
    
    def Evaluation(self):
        pass
    
    def getMetrix(self, high, low, close, days=14):
        m = Metrix()
        self._metrix = m.metrixCalculate(high, low, close, days)
        
'''
risk analysis
calculate the coefficient of earn_rate
if earn_rate more than a fix value, means this is risk
this value depend on experiment
'''
class riskAnalysis(analysis):  
    def getAnalysis(self):
        earn_rate_data = self._metrix["earn_rate"]
        earn_rate_range = np.max(earn_rate_data) - np.min(earn_rate_data)
        earn_rate_interquartile_range = np.quantile(earn_rate_data, 0.75) - np.quantile(earn_rate_data, 0.25)
        earn_rate_var = np.var(earn_rate_data)
        earn_rate_std = np.std(earn_rate_data)
        earn_rate_coefficient = earn_rate_std / np.mean(earn_rate_data)
        if earn_rate_coefficient > 10:
            return "risk"
        else:
            return "no risk"

'''
Sentiment analysis
Use Skewness refers to asymmetry deviates from normal distrubution. Use it for fundenmentional analysis
If the value more than 0 means higher profit probability 
'''
class sentimentalAnalysis(analysis):
    def getAnalysis(self):
        earn_rate_data = self._metrix["earn_rate"]
        earn_rate_skew = stats.skew(earn_rate_data)
        print(earn_rate_skew)
        print("Sentiment analysis:")
        if earn_rate_skew > 0:
            print("good")
        else:
            print("bad")

'''
technical analysis, which is depend on Monte Carlo Simulation
'''
class technicalAnalysis(analysis):
    def getAnalysis(self):
        earn_rate_data = self._metrix["earn_rate"]
        close = self._metrix["close"]
        close_data = pd.DataFrame(close)
        log_returns = np.log(1 + close_data.pct_change())

        u = log_returns.mean()
        var = log_returns.var()
        drift = u - (0.5 * var)

        stdev = log_returns.std()
        days = 50
        trials = 10000
        Z = norm.ppf(np.random.rand(days, trials))  # days, trials
        daily_returns = np.exp(drift.values + stdev.values * Z)

        price_paths = np.zeros_like(daily_returns)
        price_paths[0] = close_data.iloc[-1]
        for t in range(1, days):
            price_paths[t] = price_paths[t - 1] * daily_returns[t]

        print(f"Expected Value: ${round(pd.DataFrame(price_paths).iloc[-1].mean(), 2)}")
        print(
            f"Return: {round(100 * (pd.DataFrame(price_paths).iloc[-1].mean() - price_paths[0, 1]) / pd.DataFrame(price_paths).iloc[-1].mean(), 2)}%")
        print(f"Probability of Breakeven: {self.probs_find(pd.DataFrame(price_paths), 0, on='return')}")
        
            
    def probs_find(self, predicted, higherthan, on = 'value'):
        if on == 'return':
            predicted0 = predicted.iloc[0,0]
            predicted = predicted.iloc[-1]
            predList = list(predicted)
            over = [(i*100)/predicted0 for i in predList if ((i-predicted0)*100)/predicted0 >= higherthan]
            less = [(i*100)/predicted0 for i in predList if ((i-predicted0)*100)/predicted0 < higherthan]
        elif on == 'value':
            predicted = predicted.iloc[-1]
            predList = list(predicted)
            over = [i for i in predList if i >= higherthan]
            less = [i for i in predList if i < higherthan]
        else:
            print("'on' must be either value or return")
        return (len(over)/(len(over)+len(less)))


class fundenmentialAnalysis(analysis):
    def getAnalysis(self):
        earn_rate_data = self._metrix["earn_rate"]
        print("fundenmential")
        earn_rate_kutosis = stats.kurtosis(earn_rate_data)
        print("kutosis", earn_rate_kutosis)
        if earn_rate_kutosis > 0:
            print("This stock is Bullish")
        else:
            print("This stock is Bearish")
        
            
class RecommendationAnalysis(analysis):
    def getAnalysis(self):
        KDJ = self._metrix["KDJ"]
        RSI = self._metrix["RSI"]
        CCI = self._metrix["CCI"]
        if CCI<=-100 or RSI <= 55 or KDJ <=80:
            return "buy"
        else:
            return "sell"
