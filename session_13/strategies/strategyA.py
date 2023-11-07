from abc_strategy import abc_strategy
class StrategyA(abc_strategy):
    def ready_open_buy(self):
        if True:
            return True
    
    def ready_open_sell(self):
        if True:
            return True
    
    def ready_close_position(self):
        return True