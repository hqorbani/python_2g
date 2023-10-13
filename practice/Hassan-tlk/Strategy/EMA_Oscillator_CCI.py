from trader import trader
import pandas as pd
import talib as ta

class EMA_Oscillator(trader):
    def extend_columns(rates_frame):
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        rates_frame['ema_8'] = ta.EMA(rates_frame['close'], timeperiod = 8)
        rates_frame['ema_28'] = ta.EMA(rates_frame['close'], timeperiod = 28)

        rates_frame['ociltr_CCI_30'] = ta.CCI(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=30)
        
        return rates_frame

    #check for buy
    def ready_buy(rate_frame):
        if (((rate_frame.iloc[-3].ema_8 < rate_frame.iloc[-3].ema_28) and 
        (rate_frame.iloc[-2].ema_8 > rate_frame.iloc[-2].ema_28)) and
        rate_frame.iloc[-2].ociltr_CCI_30 > 0): 
            return True

    def ready_sell(rate_frame):
        if (((rate_frame.iloc[-3].ema_8 > rate_frame.iloc[-3].ema_28) and 
        (rate_frame.iloc[-2].ema_8 < rate_frame.iloc[-2].ema_28)) and
        rate_frame.iloc[-2].ociltr_CCI_30 < 0): 
            return True

