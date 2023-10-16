from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time
import MetaTrader5 as mt5
bot_1 = EMA_Oscillator
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    symbole  = "EURUSD_i"
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 45

def run_trader(bot_1):
    candles = bot_1.get_candles(symbole , tm , start , number)
    rate_frame = bot_1.extend_columns(candles)
    if bot_1.ready_buy(rate_frame):
        print("buy: bass on EMA_Oscillator")
        bot_1.open_position()
    elif bot_1.ready_sell(rate_frame):
        print("sell: bass on EMA_Oscillator")
    else:
        print("EMA_Oscillator have not any Ideas")

schedule.every(900).seconds.do(run_trader , bot_1)

while True:
    schedule.run_pending()
    time.sleep(1)