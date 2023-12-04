from trader import trader
import time
main_bot = trader

if main_bot.initiate():

    symbol = "EURUSD_i"
    tm = 5
    start = 0
    number = 300

    candles = main_bot.get_candles(symbol, tm, start, number)
    extend_columns = main_bot.extend_columns(candles)


for i in range(1, len(extend_columns)):
    if (extend_columns.iloc[-1].slowk_335 > 20 and
            extend_columns.iloc[-1].slowk_3314 > 20 and
            extend_columns.iloc[-2].slowk_335 < 20 and
            extend_columns.iloc[-2].slowk_3314 < 20 and
            extend_columns.iloc[-1].low > extend_columns.iloc[-1].ema_9):
        print("Buy signal")
    elif (extend_columns.iloc[-1].slowk_335 < 80 and
            extend_columns.iloc[-1].slowk_3314 < 80 and
            extend_columns.iloc[-2].slowk_335 > 80 and
            extend_columns.iloc[-2].slowk_3314 > 80 and
            extend_columns.iloc[-1].low < extend_columns.iloc[-1].ema_9):
        print("Sell signal")
    else:
        print("No signal")
