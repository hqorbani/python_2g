from trader import trader
import MetaTrader5 as mt5
bot_1 = trader
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    # for account_key , account_value in account_info.items():
    #     print(account_key,"==>" , account_value)
    symbole  = "EURUSD"
    tm = 1
    start = 0
    number = 1500
    candles = bot_1.get_candles(symbole , tm , start , number)
    # print(type(candles))
    print(candles)
    print(candles.iloc[-2].high)



    # if bot_1.check_buy():
    #      print(bot_1.open_position('buy'))
    # elif bot_1.check_sell():
    #     print(bot_1.open_position('sell'))