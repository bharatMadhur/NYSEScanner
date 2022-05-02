from main import intradayChartingPrices
import pandas as pd


# print(intradayChartingPrices(1, 2, 3))

def movingAverage(ticker, timeFrame):
    timeFrame = 7  # Remove afterwards
    incoming_d = intradayChartingPrices(1, 2, 3)
    df = pd.DataFrame(incoming_d)
    calc_ma = (df['close'].tail(timeFrame).sum()) / timeFrame
    print(calc_ma)


movingAverage(1, 2)
