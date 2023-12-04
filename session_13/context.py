class Context:
    def __init__(self, strategy_a , strategy_b):
        self._strategy_a = strategy_a
        self._strategy_b = strategy_b

    def execute_strategy(self):
        if  (self._strategy_a.ready_open_buy() and
        self._strategy_b.ready_open_buy()):
            return "buy"
        elif (self._strategy_a.ready_open_sell() and
        self._strategy_b.ready_open_sell()):
            return "sell"
        
