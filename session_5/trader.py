# for windows os:
# import MetaTrader5 as mt5
# for linux os:


class trader:
    def __init__(self, mt5) -> None:
        self.mt5 = mt5
    def connect(self):
        if self.mt5.initialize():
            return True
        else:
            return False
    def check_buy(self):
        return True
    def check_sell(self):
        return True
    def open_position(self, p_type):
        return p_type

        



