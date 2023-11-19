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
position_status = {
    "start_price" : 0,
    "p_type" : ""
}
total_point = 0
for i  in range(len(rates) - 2):
    # before candle:
    b_candle = rates.iloc[i]
    # current candle:
    c_candle = rates.iloc[i + 1]
    # next candle:
    n_candle = rates.iloc[i + 2]
    if (
        # check bearish
        b_candle.close < b_candle.open and
        # check bullish
        c_candle.close > c_candle.open and
        # check bullish
        n_candle.close > n_candle.open and
        
        c_candle.close < n_candle.open and
        c_candle.close < b_candle.close
    ):
        print(c_candle.time) 

