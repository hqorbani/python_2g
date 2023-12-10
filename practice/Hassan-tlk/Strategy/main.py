from trader import Trader
from EMA_Oscillator_CCI import EMA_Oscillator
from pattern_recog import Pattern_recog
import schedule
import time
import MetaTrader5 as mt5

prnt_bot = Trader
bot_1 = EMA_Oscillator
Pttrn_rcg = Pattern_recog

bots_lst = [prnt_bot, bot_1]

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

def run_trader(bots_lst, symbole):
    for the_bot in bots_lst:
        for sym in symbole:
            candles = the_bot.get_candles(sym , tm , start , number)
            rate_frame = the_bot.extend_columns(candles)
            if Pttrn_rcg.shooting_star(rate_frame):
                print(f"a shooting star candlestick in {sym}")
            if Pttrn_rcg.morning_star(rate_frame):
                print(f"a morning star candlestick in {sym}")
            if the_bot.ready_buy(rate_frame):
                print(f"buy on {sym}: bass on {the_bot.from_bot()}")
                the_bot.open_position(symbol_str=sym, order_type_str="buy")
            elif the_bot.ready_sell(rate_frame):
                print(f"sell on {sym}: bass on {the_bot.from_bot()}")
                the_bot.open_position(symbol_str=sym, order_type_str="sell")
            else:
                print(f"{the_bot.from_bot()} have no Ideas about {sym}")
        print("===============",candles.iloc[-1].time,"====================")

schedule.every(5).seconds.do(run_trader , bots_lst, symbole)

while True:
    schedule.run_pending()
    time.sleep(1)