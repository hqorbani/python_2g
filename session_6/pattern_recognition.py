from trader import trader
from strategies.ema import ema
# from strategies.ema import ema
import schedule
import time

bot_1 = trader
my_strategy = ema
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbol  = "EURJPY_i"
    tm = 1
    start = 0
    number = 1500

def get_cols(bot_1):
    candles = bot_1.get_candles(symbol , tm , start , number)
    return my_strategy.extend_columns(candles)
    

rates = get_cols(bot_1)

for i in range(len(rates)):
    # if rates.iloc[i].shooting_star in [100 , -100]:
    #     print(rates.iloc[i].time , rates.iloc[i].open , rates.iloc[i].shooting_star )
    if rates.iloc[i].morning_star in [100 , -100]:
        print(rates.iloc[i].time , rates.iloc[i].open , rates.iloc[i].morning_star )