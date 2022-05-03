from main import fundamentalDow30
import pandas as pd


def swotAnalysis(ticker):
    stren=[]
    weak =[]
    oppur=[]
    threat=[]
    incoming_d = fundamentalDow30(ticker)
    df = pd.DataFrame(incoming_d)
    print(df.T)
    print()
    if df.iloc[0]['marketCap'] <100 :
        oppur.append("Small Cap")
        threat.append("Small Cap")
    else:
        stren.append("established Company")
    if df.iloc[0]['enterpriseVal'] > 10:
        threat.append("Scary enterprise Val")
    else:
        stren.append("good enterprise Val")
        oppur.append("good enterprise Val")
    if df.iloc[0]['peRatio'] > 25:
        threat.append("OverValued")
        weak.append("Poor peRatio")
    else:
        stren.append("Undervalued")
        oppur.append("Undervalued")
    if df.iloc[0]['pbRatio'] > 1.5:
        threat.append("poor pbRatio")
    else:
        stren.append("Good PbRatio")
        oppur.append("Lucrative PbRatio")
    if df.iloc[0]['trailingPEG1Y'] > 1:
        threat.append("isn't necessarily supported by growth forecasts")
        weak.append("isn't necessarily supported by growth forecasts")
    else:
        stren.append("not currently accounting for expected earnings growth")
        oppur.append("not currently accounting for expected earnings growth")
    # x=df.loc[df['Name'].str.contains("pokemon", case=False)]
    return stren, weak, oppur, threat



