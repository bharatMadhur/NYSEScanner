from main import intradayChartingPrices
import pandas as pd


# print(intradayChartingPrices(1, 2, 3))

def pivot_level(ticker):
    timeFrame = 7  # Remove afterwards
    incoming_d = intradayChartingPrices(1, 2, 3)
    df = pd.DataFrame(incoming_d)

    # pivot_point=0 'high', 'low','close'
    curr_high, curr_low, curr_close = df['high'].tail(1), df['low'].tail(1), df['close'].tail(1)
    pivot_point = (curr_low + curr_high + curr_close) / 3

    resistance_r1 = (2 * pivot_point) - df['low'].tail(1)
    support_s1 = (2 * pivot_point) - df['high'].tail(1)
    resistance_r2 = pivot_point + (df['high'].tail(1) - df['low'].tail(1))
    support_s2 = pivot_point - (df['high'].tail(1) - df['low'].tail(1))
    resistance_r3 = df['high'].tail(1) + (2 * (pivot_point - df['low'].tail(1)))
    support_s3 = df['low'].tail(1) - (2 * (df['high'].tail(1) - pivot_point))



pivot_level(1)
