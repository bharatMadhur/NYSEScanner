from main import intradayChartingPrices
import pandas as pd


# print(intradayChartingPrices(1, 2, 3))

def movingAverage(ticker, timeFrame):
    #timeFrame = 7  # Remove afterwards
    incoming_d = intradayChartingPrices(1, ticker, 1)
    df = pd.DataFrame(incoming_d)
    calc_ma = (df['close'].tail(timeFrame).sum()) / timeFrame
    return calc_ma


movingAverage("msft", 7)

def chartMovingAverage(ticker, timeFrame):
    incoming_d = intradayChartingPrices(1, ticker, 1)
    df = pd.DataFrame(incoming_d)
    series_mv =[df.loc[1,"close"],((df.loc[1,"close"]+df.loc[2,"close"])/2),((df.loc[1,"close"]+df.loc[2,"close"]+df.loc[3,"close"])/3),((df.loc[1,"close"]+df.loc[2,"close"]+df.loc[3,"close"]+df.loc[5,"close"])/4)]
    for i in range(timeFrame, len(df)):
        temp = i if i in [0, 1] else (df.loc[i - (timeFrame-1), 'close'] + df.loc[i - (timeFrame-1), 'close']+df.loc[i - (timeFrame-1), 'close']+df.loc[i - (timeFrame-1), 'close'])/ timeFrame
        series_mv.append(temp)

    #calc_ma = (df['close'].tail(timeFrame).sum()) / timeFrame
    return series_mv

chartMovingAverage("msft", 4)

