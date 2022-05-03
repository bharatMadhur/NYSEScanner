from datetime import datetime
from dateutil.relativedelta import relativedelta
from main import endOfTheDay
import pandas as pd


def yoyprofitgrowth(ticker):
    one_year_ago = datetime.now() - relativedelta(years=1)
    df=pd.DataFrame(endOfTheDay(ticker, one_year_ago.date()))
    print(df.iloc[-1]['close'])
    print(df.iloc[0]['close'] - df.iloc[-1]['close'])
    return df.iloc[0]['close'] - df.iloc[-1]['close']


