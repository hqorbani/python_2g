import pandas as pd
from trader import trader
from EMA_Oscillator_CCI import EMA_Oscillator
import schedule
import time
import MetaTrader5 as mt5
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
bot_1 = EMA_Oscillator
if bot_1.connect():
    # account_info = bot_1.get_account_info()
    symbole  = ["EURUSD_i", "EURGBP_i", "XAUUSD_i", "NQ100_m_i"]
    tm = mt5.TIMEFRAME_H1 # TIMEFRAME_M30
    start = 0
    number = 45
    # symbol_info=mt5.symbol_info("EURJPY_i")
    # if symbol_info!=None:
    #     # display the terminal data 'as is'    
    #     print(symbol_info)
    #     print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
    #     # display symbol properties\ as a list
    #     print("Show symbol_info(\"EURJPY\")._asdict():")
    #     symbol_info_dict = mt5.symbol_info("EURJPY_i")._asdict()
    #     for prop in symbol_info_dict:
    #         print("  {}={}".format(prop, symbol_info_dict[prop]))

    # get the list of positions on symbols whose names contain "*USD*"
    # usd_positions=mt5.positions_get(group="*USD*")
    # if usd_positions==None:
    #     print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
    # elif len(usd_positions)>0:
    #     print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    #     # display these positions as a table using pandas.DataFrame
    #     df=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())
    #     df['time'] = pd.to_datetime(df['time'], unit='s')
    #     df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    #     print(df)

    # account_info=mt5.account_info()
    # if account_info!=None:
    #     # display trading account data 'as is'
    #     print(account_info)
    #     # display trading account data in the form of a dictionary
    #     print("Show account_info()._asdict():")
    #     account_info_dict = mt5.account_info()._asdict()
    #     for prop in account_info_dict:
    #         print("  {}={}".format(prop, account_info_dict[prop]))
    #     print()
    #     print(account_info_dict["margin_free"])

    
else:
    print("Disconnect")


d = "0"*5
print(d)
d = "1"+d
print(type(d))