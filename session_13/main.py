from context import Context
from strategies.strategyA import StrategyA
from strategies.strategyB import StrategyB

# استفاده از الگوریتم استراتژی
strategy_a = StrategyA()
strategy_b = StrategyB()

context = Context(strategy_a , strategy_b)
print(context.execute_strategy())
