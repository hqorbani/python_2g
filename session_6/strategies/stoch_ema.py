import pandas as pd
import talib as ta
class stoch_ema:
    def extend_columns(rates_frame):
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        rates_frame['ema_9'] = ta.EMA(rates_frame['close'], timeperiod = 9)
        rates_frame['slowk_335'], rates_frame['slowd_335'] = ta.STOCH(rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        rates_frame['slowk_3314'], rates_frame['slowd_3314'] = ta.STOCH(rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        return rates_frame
    #check for buy
    def ready_buy(rate_frame):
        if (rate_frame.iloc[-2].slowk_335 > 20 and
            rate_frame.iloc[-2].slowk_3314 > 20 and 
            rate_frame.iloc[-3].slowk_335 < 20  and
            rate_frame.iloc[-3].slowk_3314 < 20 and
            rate_frame.iloc[-2].low > rate_frame[-2].ema_9):
            return True

    def ready_sell(rate_frame):
        if (rate_frame.iloc[-2].slowk_335 < 80 and
            rate_frame.iloc[-2].slowk_3314 < 80 and 
            rate_frame.iloc[-3].slowk_335 > 80  and
            rate_frame.iloc[-3].slowk_3314 > 80 and
            rate_frame.iloc[-2].high < rate_frame[-2].ema_9):
            return True
