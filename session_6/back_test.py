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
    number = 150

def get_cols(bot_1):
    candles = bot_1.get_candles(symbol , tm , start , number)
    return my_strategy.extend_columns(candles)
    

rates = get_cols(bot_1)
position_status = {
    "start_price" : 0,
    "p_type" : ""
}
total_point = 0
for i  in range(len(rates) - 1):
    point = 0
    # check to there is open position
    if position_status["start_price"] == 0:
        if (
            rates.iloc[i].ema_9 < rates.iloc[i].ema_20 and
            rates.iloc[i+1].ema_9 > rates.iloc[i+1].ema_20
        ):
            position_status["start_price"] = rates.iloc[i+1].open
            position_status["p_type"] = "buy"
            print("start buy: ", rates.iloc[i+1].time , rates.iloc[i+1].open)
        elif(
            rates.iloc[i].ema_9 > rates.iloc[i].ema_20 and
            rates.iloc[i+1].ema_9 < rates.iloc[i+1].ema_20
        ):
            position_status["start_price"] = rates.iloc[i+1].open
            position_status["p_type"] = "sell"
            print("start sell: ", rates.iloc[i+1].time , rates.iloc[i+1].open)
    elif (
            position_status["p_type"] == "buy" and
            rates.iloc[i].ema_9 > rates.iloc[i].ema_20 and
            rates.iloc[i+1].ema_9 < rates.iloc[i+1].ema_20
        ):
        end_price = rates.iloc[ i + 1].close
        point = end_price - position_status["start_price"] - rates.iloc[i+1].spread
        print("end buy: ", rates.iloc[i+1].time , rates.iloc[i+1].close , "points:", point)
        #----
        position_status["start_price"] = rates.iloc[i+1].open
        position_status["p_type"] = "sell"
        print("start sell: ", rates.iloc[i+1].time , rates.iloc[i+1].open)

    elif (
        position_status["p_type"]=="sell" and
        rates.iloc[i].ema_9 < rates.iloc[i].ema_20 and
        rates.iloc[i+1].ema_9 > rates.iloc[i+1].ema_20
    ):
        end_price = rates.iloc[ i + 1].close
        point = position_status["start_price"] - end_price - rates.iloc[i+1].spread
        print("end sell: ", rates.iloc[i+1].time , rates.iloc[i+1].close , "points:", point)
        #---
        position_status["start_price"] = rates.iloc[i+1].open
        position_status["p_type"] = "buy"
        print("start buy: ", rates.iloc[i+1].time , rates.iloc[i+1].open)
    total_point += point
print()
print("total points:" , total_point)