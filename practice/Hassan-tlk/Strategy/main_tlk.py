from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time

bot_1 = EMA_Oscillator
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbole  = "EURUSD_i"
    tm = 1
    start = 0
    number = 45

def run_trader(bot_1):
    candles = bot_1.get_candles(symbole , tm , start , number)
    rate_frame = bot_1.extend_columns(candles)
    if bot_1.ready_buy(rate_frame):
        print("buy: bass on EMA_Oscillator")
    elif bot_1.ready_sell(rate_frame):
        print("sell: bass on EMA_Oscillator")
    else:
        print("EMA_Oscillator have not any Ideas")

schedule.every(10).seconds.do(run_trader , bot_1)

while True:
    schedule.run_pending()
    time.sleep(1)