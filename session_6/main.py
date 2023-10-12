from trader import trader
from strategies.stoch_ema import stoch_ema
import schedule
import time

bot_1 = trader
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbole  = "EURUSD"
    tm = 1
    start = 0
    number = 15

def run_trader(bot_1):
    candles = bot_1.get_candles(symbole , tm , start , number)
    rate_frame = bot_1.extend_columns(candles)
    if bot_1.ready_buy(rate_frame):
        print("do buy")
    elif bot_1.ready_sell(rate_frame):
        print("do sell")
    else:
        print("nothing")

schedule.every(3).seconds.do(run_trader , bot_1)

while True:
    schedule.run_pending()
    time.sleep(1)