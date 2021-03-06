# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:06:43 2022

@author: ycgao
"""

import requests
from datetime import datetime, timedelta

x = "aapl"


today = datetime.today()
thirty_days_ago = today - timedelta(days=90)
print(type(thirty_days_ago))

#date_time = thirty_days_ago.strftime("%m-%d-%Y")
date_time = thirty_days_ago.strftime("%Y-%m-%d")
print(date_time)
headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/"+x+"/prices?startDate="+date_time+"&token=2f7e85db1869a38072f3348bdae03512c8438e30", headers=headers)
print(requestResponse.json())

import numpy as np

close=[]
high=[]
low=[]
open_price=[]
volume=[]


datas = requestResponse.json()
print('Days:', len(datas))
for data in datas:
    open_price.append(data['open'])
    close.append(data['close'])
    high.append(data['high'])
    low.append(data['low'])
    volume.append(data['volume'])

import numpy as np
close=np.array(close)
high=np.array(high)
low=np.array(low)
open_price=np.array(open_price)
volume=np.array(volume)

'''
recommendation is depend on three targets:KDJ RSI and CCI
    
'''
def KDJ(high, low, close):
    K=50
    D=50
    for i in range(high.shape[0]):
        RSV = (close[i]-low[i])/(high[i]-low[i])
        K = 2/3*K+1/3*RSV
        D = 2/3*D+1/3*K
    J = 3*D-2*K
    return J

def RSI(close, days): #Relative Strength Index
    import numpy as np
    closeRSI = close[close.shape[0]-days-1:close.shape[0]]
    closeDiff = np.diff(closeRSI)
    riseIndex = np.where(closeDiff>=0)
    downIndex = np.where(closeDiff<=0)
    a = sum(closeDiff[riseIndex])
    b = -1*sum(closeDiff[downIndex])
    RSI = a/(a+b)*100
    return RSI

def CCI(high, low ,close, days):
    TP = (high[-1]+low[-1]+close[-1])/3
    MA = sum(close[close.shape[0]-days-1:close.shape[0]])/len(close[close.shape[0]-days-1:close.shape[0]])
    MD = sum(abs(MA-close[close.shape[0]-days-1:close.shape[0]]))/len(close[close.shape[0]-days-1:close.shape[0]])
    #print(MD)
    CCI = 1/0.015*(TP-MA)/MD
    return CCI

J = KDJ(high, low, close)
RSINum = RSI(close, 10)
CCINum = CCI(high, low, close, 7)

def recommendation(KDJ, RSI, CCI):
    if CCI<=-100 or RSI <= 55 or KDJ <=80:
        return list([0, CCI, KDJ, RSI])
    else:
        return list([0, CCI, KDJ, RSI])

stockTelAnalysis = recommendation(J, RSINum, CCINum)

'''
risk analysis
calculate the coefficient of earn_rate
if earn_rate more than a fix value, means this is risk
this value depend on experiment
'''
earn_rate_data = (close[1:]-close[0:close.shape[0]-1])/close[0:close.shape[0]-1]
earn_rate_range=np.max(earn_rate_data)-np.min(earn_rate_data)
earn_rate_interquartile_range=np.quantile(earn_rate_data, 0.75)-np.quantile(earn_rate_data, 0.25)
earn_rate_var=np.var(earn_rate_data)
earn_rate_std=np.std(earn_rate_data)
earn_rate_coefficient=np.std(earn_rate_data)/np.mean(earn_rate_data)
print("risk analysis:")
print("coefficient:",earn_rate_coefficient)
if earn_rate_coefficient>10:
    print("risk")

'''
Sentiment analysis
Use Skewness refers to asymmetry deviates from normal distrubution. Use it for fundenmentional analysis
If the value more than 0 means higher profit probability 
'''
from scipy import stats
earn_rate_skew=stats.skew(earn_rate_data)
print("Sentiment analysis:")
if earn_rate_skew>0:
    print("good")
else:
    print("bad")
    
'''
fundenmential analysis, which is depend on Monte Carlo Simulation
'''
print
import numpy as np
import pandas as pd
#from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

close_data = pd.DataFrame(close)
log_returns = np.log(1 + close_data.pct_change())
##Plot
sns.distplot(log_returns.iloc[1:])
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5*var)

stdev = log_returns.std()
days = 50
trials = 10000
Z = norm.ppf(np.random.rand(days, trials)) #days, trials
daily_returns = np.exp(drift.values + stdev.values * Z)

price_paths = np.zeros_like(daily_returns)
price_paths[0] = close_data.iloc[-1]
for t in range(1, days):
    price_paths[t] = price_paths[t-1]*daily_returns[t]
    
def probs_find(predicted, higherthan, on = 'value'):
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
    
print(f"Expected Value: ${round(pd.DataFrame(price_paths).iloc[-1].mean(),2)}")
print(f"Return: {round(100*(pd.DataFrame(price_paths).iloc[-1].mean()-price_paths[0,1])/pd.DataFrame(price_paths).iloc[-1].mean(),2)}%")
print(f"Probability of Breakeven: {probs_find(pd.DataFrame(price_paths),0, on='return')}")

'''
fundenmential analysis
'''
print("fundenmential")
earn_rate_kutosis=stats.kurtosis(earn_rate_data)
print("kutosis", earn_rate_kutosis)
if earn_rate_kutosis>0:
    prnit("This stock could bring high profit")
else:
    print("This stock could not bring too much profit")