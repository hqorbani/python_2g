import MetaTrader5 as mt5

class trader:
    # def __init__(self, username) -> None:
    #     self.username = username
    def connect():
        if mt5.initialize():
            return True
        else:
            return False
    def check_buy():
        return True
    def check_sell():
        return True
    def open_position(p_type):
        return p_type

        



