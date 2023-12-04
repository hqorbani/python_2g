from trader import trader
from mt5linux import MetaTrader5

mt5 = MetaTrader5(
    host = 'localhost' ,
    port = 18812      
)
bot_1 = trader(mt5)
if bot_1.connect():
    if bot_1.check_buy():
         print(bot_1.open_position('buy'))
    elif bot_1.check_sell():
        print(bot_1.open_position('sell'))