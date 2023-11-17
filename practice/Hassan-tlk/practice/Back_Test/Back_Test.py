from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time
import MetaTrader5 as mt5
bot_1 = EMA_Oscillator
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    sym = "EURUSD_i"
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 150
    candles = bot_1.get_candles(sym , tm , start , number)
    rate_frame = bot_1.extend_columns(candles)
    # print(rate_frame)
    # time     open     high      low    close  spread     ema_8    ema_28  ociltr_CCI_30

    buy = {}
    sell = {}
    possition_status = {
        "start_price": 0,
        "p_type": ""
    }
    total_point = 0
    for i in range(31, number-5):
        point = 0
        if possition_status["start_price"] == 0:
            if (((rate_frame.iloc[i].ema_8 < rate_frame.iloc[i].ema_28) and 
            (rate_frame.iloc[i+1].ema_8 > rate_frame.iloc[i+1].ema_28)) and
            rate_frame.iloc[i+1].ociltr_CCI_30 > 0):
                possition_status["start_price"] = rate_frame.iloc[i+1].open
                possition_status["p_type"] = "buy"
                buy_temp = {}
                buy_temp.update({"time": rate_frame.iloc[i+1]["time"]})
                buy_temp.update({"close": rate_frame.iloc[i+1]["close"]})
                buy.update({str(i): buy_temp})

            elif (((rate_frame.iloc[i].ema_8 > rate_frame.iloc[i].ema_28) and 
            (rate_frame.iloc[i+1].ema_8 < rate_frame.iloc[i+1].ema_28)) and
            rate_frame.iloc[i+1].ociltr_CCI_30 < 0):
                possition_status["start_price"] = rate_frame.iloc[i+1].open
                possition_status["p_type"] = "sell"
                sell_temp = {}
                sell_temp.update({"time": rate_frame.iloc[i+1]["time"]})
                sell_temp.update({"close": rate_frame.iloc[i+1]["close"]})
                sell.update({str(i): sell_temp})

        elif (possition_status["p_type"] == "buy" and ((rate_frame.iloc[i+2].ema_8 > rate_frame.iloc[i+2].ema_28) and (rate_frame.iloc[i+1].ema_8 < rate_frame.iloc[i+1].ema_28)) and rate_frame.iloc[i+1].ociltr_CCI_30 < 0):
            end_price = rate_frame.iloc[i].close
            point = end_price - possition_status["start_price"] - rate_frame.iloc[i].spread
            possition_status["start_price"] = rate_frame.iloc[i].open
            possition_status["p_type"] = "sell"
            total_point += point

        elif (possition_status["p_type"] == "sell" and ((rate_frame.iloc[i+2].ema_8 < rate_frame.iloc[i+2].ema_28) and (rate_frame.iloc[i+1].ema_8 > rate_frame.iloc[i+1].ema_28)) and rate_frame.iloc[i+1].ociltr_CCI_30 > 0):
            end_price = rate_frame.iloc[i].close
            point = end_price - possition_status["start_price"] - rate_frame.iloc[i].spread
            possition_status["start_price"] = rate_frame.iloc[i].open
            possition_status["p_type"] = "buy"
            total_point += point





    print("buy:\n", buy)
    print("sell:\n", sell)
    print("total_point:\n", total_point)


else: #connection
    print("Connection is lost")