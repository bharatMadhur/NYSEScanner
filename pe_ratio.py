from main import fundamentalDow30
# from main import fundamentalsDow30
import pandas as pd


def peAnalysis(ticker):
    incoming_d = fundamentalDow30()
    df = pd.DataFrame(incoming_d)
    if df.iloc[0]['peRatio'] > 0:
        return "The Company is Profitable", df.iloc[0]['peRatio']


print(peAnalysis(1))
