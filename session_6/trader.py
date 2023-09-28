import MetaTrader5 as mt5
# import pandas as pd
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

    def get_candles():
        # این متد قراره اطلاعات کندلی مربوط به 15 کندل اخیر را دریافت کند
        # ورودی های متد را خودتان مشخص کنید
        pass

    
        



