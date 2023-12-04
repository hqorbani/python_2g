# from trader import trader
from STAR_pattern_class import StarPattern
import schedule
import time
import MetaTrader5 as mt5

bot_1 = StarPattern
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    symbole  = ["EURUSD_i", "EURGBP_i", "XAUUSD_i", "NQ100_m_i"]
    tm = mt5.TIMEFRAME_M30 # TIMEFRAME_H1
    start = 0
    number = 15

def run_trader(bot_1, symbole):
    for sym in symbole:
        candles = bot_1.get_candles(sym , tm , start , number)
        print(candles.iloc[-1].time)
        if bot_1.morning_star(candles):
            print("Morning Star Pattern")
        elif bot_1.evening_star(candles):
            print("Evening Star Pattern")
        else:
            print(f"Star Pattern have no Ideas about {sym}")
    print("===============",candles.iloc[-1].time,"====================")

schedule.every(11).seconds.do(run_trader , bot_1, symbole)

while True:
    schedule.run_pending()
    time.sleep(1)
