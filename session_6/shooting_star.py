from trader import trader
import talib as ta
# from strategies.ema import ema
import schedule
import time

bot_1 = trader
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbol  = "NQ100_m_i"
    tm = 5
    start = 0
    number = 3000
def shooting_star_m(candles):
    candles['shooting_star_m'] = 0
    for i in range(len(candles) - 1):
        # check bullish:
        if candles.iloc[i].open < candles.iloc[i].close:
            if (((candles.iloc[i].high - candles.iloc[i].close) / 3) >= (candles.iloc[i].close - candles.iloc[i].open) and
            ((candles.iloc[i].close - candles.iloc[i].open) / 5) > (candles.iloc[i].open - candles.iloc[i].low)):
                print("---", candles.iloc[i].time)
                candles.iloc[i].shooting_star_m = 100
        elif (
            ((candles.iloc[i].high - candles.iloc[i].open) / 3) >= (candles.iloc[i].open - candles.iloc[i].close) and
            ((candles.iloc[i].open - candles.iloc[i].close) / 5) > (candles.iloc[i].close - candles.iloc[i].low)
        ):
            candles.iloc[i].shooting_star_m = -100
    return candles
def get_cols(bot_1):
    candles = bot_1.get_candles(symbol , tm , start , number)
    candles['shooting_star'] = ta. CDLSHOOTINGSTAR(candles['open'], candles['high'], candles['low'], candles['close'])
    return shooting_star_m(candles)
    

rates = get_cols(bot_1)

total_point = 0
for i  in range(len(rates) - 2):
    if rates.iloc[i].shooting_star in [100.0 , -100.0] or rates.iloc[i].shooting_star_m in [100.0 , -100.0]:
        print(rates.iloc[i].time , rates.iloc[i].shooting_star , rates.iloc[i].shooting_star_m ) 

