import pandas as pd
import talib as ta
class ema:
    def extend_columns(rates_frame):
        rates_frame['ema_9'] = ta.EMA(rates_frame['close'], timeperiod = 9)
        rates_frame['ema_20'] = ta.EMA(rates_frame['close'], timeperiod = 20)
        return rates_frame
    #check for buy
    def ready_buy(rate_frame):
        if (rate_frame.iloc[-2].ema_9 > rate_frame.iloc[-2].ema_20 and
            rate_frame.iloc[-3].ema_9 < rate_frame.iloc[-3].ema_20):
            return True

    def ready_sell(rate_frame):
        if (rate_frame.iloc[-2].ema_9 < rate_frame.iloc[-2].ema_20 and
            rate_frame.iloc[-3].ema_9 > rate_frame.iloc[-3].ema_20):
            return True