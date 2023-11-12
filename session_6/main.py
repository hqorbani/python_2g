from trader import trader
from strategies.stoch_ema import stoch_ema
# from strategies.ema import ema
import schedule
import time

bot_1 = trader
my_strategy = stoch_ema
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbol  = "EURJPY_i"
    tm = 1
    start = 0
    number = 15

def run_trader(bot_1):
    candles = bot_1.get_candles(symbol , tm , start , number)
    rate_frame = my_strategy.extend_columns(candles)
    print(rate_frame)
    if my_strategy.ready_buy(rate_frame):
        bot_1.open_position(symbol ,"buy" , 0.01)
        print("do buy")
    elif my_strategy.ready_sell(rate_frame):
        bot_1.open_position(symbol , "sell" , 0.01)
        print("do sell")
    else:
        print("nothing")

schedule.every(3).seconds.do(run_trader , bot_1)

while True:
    schedule.run_pending()
    time.sleep(1)