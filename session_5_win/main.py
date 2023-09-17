from trader import trader

bot_1 = trader
if bot_1.connect():
    account_info = bot_1.get_account_info()
    for account_key , account_value in account_info.items():
        print(account_key,"==>" , account_value)


    # if bot_1.check_buy():
    #      print(bot_1.open_position('buy'))
    # elif bot_1.check_sell():
    #     print(bot_1.open_position('sell'))