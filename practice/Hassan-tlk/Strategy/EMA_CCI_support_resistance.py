from trader import trader
import pandas as pd
import talib as ta
import MetaTrader5 as mt5
import json

class EMA_CCI_support_resistance(trader):
    def extend_columns(rate_frame):
        rate_frame['time'] = pd.to_datetime(rate_frame['time'] , unit= 's')
        return rate_frame

    def base_line_by_hassan(rate_frame):
        colum = [0]
        for i in range(number, 1, -1):
            if i > number-27:
                colum.append(0)
                continue
            for j in range(26,1,-1):
                high_lst = []
                high_lst.append(rate_frame.iloc[i+j].high)
                low_lst = []
                low_lst.append(rate_frame.iloc[i+j].high)
            high_max, low_max = max(high_lst), max(low_lst)
            high_min, low_min = min(high_lst), min(low_lst)
            Kijun_sen = (high_max+low_min)/2
            colum.append(Kijun_sen)
        rate_frame['Kijun_sen'] = colum
        # print(len(colum))
        return rate_frame
    
    def base_line_by_AI(rate_frame):
        period_high = rate_frame['high'].rolling(window=26).max()
        period_low = rate_frame['low'].rolling(window=26).min()
        Kijun_sen = (period_high+period_low)/2
        rate_frame['Kijun_sen'] = Kijun_sen
        return rate_frame


bot_1 = EMA_CCI_support_resistance

if bot_1.connect():
    symbole  = "EURUSD_i"
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 100

# vvvvvvvvvvvvvvvvvvv TEST vvvvvvvvvvvvvvvvvvv
    candles = bot_1.get_candles("EURUSD_i" , tm , start , number)
    rate_frame = bot_1.extend_columns(candles)
    rate_frame = bot_1.base_line_by_AI(rate_frame)
    for i in range(len(rate_frame)):
        print(i, rate_frame.iloc[i].time, "==>",rate_frame.iloc[i].Kijun_sen)
# ^^^^^^^^^^^^^^^^^^^ TEST ^^^^^^^^^^^^^^^^^^^
