from main import fundamentalDow30
import pandas as pd


def swotAnalysis(ticker):
    incoming_d = fundamentalDow30()
    df = pd.DataFrame(incoming_d)
    print(df.T)
    print()
    if df.iloc[0]['marketCap'] > 100:
        print("Madhur is tbe Best")
    if df.iloc[0]['enterpriseVal'] > 100:
        print("Madhur is tbe Best")
    if df.iloc[0]['peRatio'] > 100:
        print("Madhur is tbe Best")
    if df.iloc[0]['pbRatio'] > 100:
        print("Madhur is tbe Best")
    if df.iloc[0]['trailingPEG1Y'] > 100:
        print("Madhur is tbe Best")
    # x=df.loc[df['Name'].str.contains("pokemon", case=False)]
    pass


swotAnalysis(1)
