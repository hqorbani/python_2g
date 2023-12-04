<<<<<<< HEAD
from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time
import MetaTrader5 as mt5
bot_1 = EMA_Oscillator
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    symbole  = ["EURUSD_i", "EURGBP_i", "XAUUSD_i", "NQ100_m_i"]
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 45

def run_trader(bot_1, symbole):
    for sym in symbole:
        candles = bot_1.get_candles(sym , tm , start , number)
        rate_frame = bot_1.extend_columns(candles)
        if bot_1.ready_buy(rate_frame):
            print(f"buy on {sym}: bass on EMA_Oscillator")
            bot_1.open_position(symbol_str=sym, order_type=mt5.ORDER_TYPE_BUY)
        elif bot_1.ready_sell(rate_frame):
            print(f"sell on {sym}: bass on EMA_Oscillator")
            bot_1.open_position(symbol_str=sym, order_type=mt5.ORDER_TYPE_SELL)
        else:
            print(f"EMA_Oscillator have no Ideas about {sym}")

schedule.every(20).seconds.do(run_trader , bot_1, symbole)

while True:
    schedule.run_pending()
=======
from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time
import MetaTrader5 as mt5
bot_1 = EMA_Oscillator
risk_percent = 2

if bot_1.connect():
    data = bot_1.read_json()
    symbole  = data.keys()
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 100

# vvvvvvvvvvvvvvvvvvv TEST vvvvvvvvvvvvvvvvvvv
    # candles = bot_1.get_candles("EURUSD_i" , tm , start , number)
    # rate_frame = bot_1.extend_columns(candles)
    # print(rate_frame)
    # bot_1.open_position(symbol_str="EURGBP_i", order_type_str="buy")
# ^^^^^^^^^^^^^^^^^^^ TEST ^^^^^^^^^^^^^^^^^^^

def run_trader(bot_1, symbole):
    for sym in symbole:
        candles = bot_1.get_candles(sym , tm , start , number)
        rate_frame = bot_1.extend_columns(candles)
        if bot_1.shooting_star(rate_frame):
            print(f"a shooting star candlestick in {sys}")
        if bot_1.ready_buy(rate_frame):
            print(f"buy on {sym}: bass on EMA_Oscillator")
            bot_1.open_position(symbol_str=sym, order_type_str="buy")
        elif bot_1.ready_sell(rate_frame):
            print(f"sell on {sym}: bass on EMA_Oscillator")
            bot_1.open_position(symbol_str=sym, order_type_str="sell")
        else:
            print(f"EMA_Oscillator have no Ideas about {sym}")
    print("===============",candles.iloc[-1].time,"====================")

schedule.every(5).seconds.do(run_trader , bot_1, symbole)

while True:
    schedule.run_pending()
>>>>>>> f339195f95f8221168d5f3ba064a3c9ec29f0ad5
    time.sleep(1)