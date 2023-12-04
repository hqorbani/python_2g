from trader import trader 

bot_1 = trader
if bot_1.connect():
    if bot_1.check_buy():
         print(bot_1.open_position('buy'))
    elif bot_1.check_sell():
        print(bot_1.open_position('sell'))