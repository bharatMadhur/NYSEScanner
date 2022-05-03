from main import fundamentalDow30
# from main import fundamentalsDow30
import pandas as pd


def peAnalysis(ticker):
    incoming_d = fundamentalDow30(ticker)
    df = pd.DataFrame(incoming_d)
    if df.iloc[0]['peRatio'] > 0:
        return df.iloc[0]['peRatio']



