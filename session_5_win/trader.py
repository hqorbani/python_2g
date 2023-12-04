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
    


    def check_buy():
        return True
    def check_sell():
        return True
    def open_position(p_type):
        return p_type

        



