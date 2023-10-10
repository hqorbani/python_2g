import MetaTrader5 as mt5
import pandas as pd
import talib as ta
class trader:
    # def __init__(self, username) -> None:
    #     self.username = username
    def connect():
        if mt5.initialize():
            return True
        else:
            return False
        
    def get_account_info():
        return mt5.account_info()._asdict()
    
    def get_symbols(str_symbols):
        return mt5.symbols_get(str_symbols)

    def get_candles(symbole , tm , start , number):
        # symbole , tm , start , number 
        # این متد قراره اطلاعات کندلی مربوط به 15 کندل اخیر را دریافت کند
        # ورودی های متد را خودتان مشخص کنید
        rates = mt5.copy_rates_from_pos(symbole , tm , start , number)
        rates_frame = pd.DataFrame(rates)
        rates_frame.drop('real_volume' , inplace = True , axis= 1)
        rates_frame.drop('tick_volume' , inplace = True , axis= 1)
        return rates_frame

    def extend_columns(rates_frame):
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        rates_frame['ema_9'] = ta.EMA(rates_frame['close'], timeperiod = 9)
        rates_frame['ema_9'] = ta.EMA(rates_frame['close'], timeperiod = 9)
        rates_frame['slowk_335'], rates_frame['slowd_335'] = ta.STOCH(rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        rates_frame['slowk_3314'], rates_frame['slowd_3314'] = ta.STOCH(rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        return rates_frame
    #check for buy
    def ready_buy(rate_frame):
        if (rate_frame.iloc[-1].slowk_335 > 20 and
            rate_frame.iloc[-1].slowk_3314 > 20 and 
            rate_frame.iloc[-2].slowk_335 < 20  and
            rate_frame.iloc[-2].slowk_3314 < 20 and
            rate_frame.iloc[-1].low > rate_frame[-1].ema_9):
            return True

    def ready_sell(rate_frame):
        if (rate_frame.iloc[-1].slowk_335 < 80 and
            rate_frame.iloc[-1].slowk_3314 < 80 and 
            rate_frame.iloc[-2].slowk_335 > 80  and
            rate_frame.iloc[-2].slowk_3314 > 80 and
            rate_frame.iloc[-1].high < rate_frame[-1].ema_9):
            return True

    
        



