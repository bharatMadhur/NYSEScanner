from datetime import datetime
from dateutil.relativedelta import relativedelta
from main import endOfTheDay
import pandas as pd


def indexComparison(ticker):
    one_year_ago = datetime.now() - relativedelta(years=1)
    index1 = endOfTheDay('INDEX', one_year_ago.date())  # INDEX: S&P 500(R) EQUAL WEIGHT NO LOAD SHARES
    index2 = endOfTheDay('NASDX', one_year_ago.date())  # NASDX: NASDAQ-100 INDEX FUND DIRECT SHARES
    df = pd.DataFrame(endOfTheDay(ticker, one_year_ago.date()))
    index1_df = pd.DataFrame(index1)
    index1_comparison = (index1_df.iloc[0]['close'] - index1_df.iloc[-1]['close'])-(df.iloc[0]['close'] - df.iloc[-1]['close'])
    index2_df = pd.DataFrame(index2)
    index2_comparison = (index2_df.iloc[0]['close'] - index2_df.iloc[-1]['close']) - (df.iloc[0]['close'] - df.iloc[-1]['close'])
    print(index1_comparison,index2_comparison)
    return index1_comparison,index2_comparison


indexComparison('msft')

