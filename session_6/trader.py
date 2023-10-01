import MetaTrader5 as mt5
import pandas as pd
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
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        # rates_frame['new_open'] = rates_frame['open'] + 2
        return rates_frame


    
        



