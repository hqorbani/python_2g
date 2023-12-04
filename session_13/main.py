from context import Context
from strategies.strategyA import StrategyA
from strategies.strategyB import StrategyB

# استفاده از الگوریتم استراتژی
strategy_a = StrategyA()
strategy_b = StrategyB()

context = Context(strategy_a , strategy_b)

if context.execute_strategy() == "buy":
    print(context.execute_strategy())

elif context.execute_strategy() == "sell":
    # pass
    # open position
    print(context.execute_strategy())
