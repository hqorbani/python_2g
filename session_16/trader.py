import MetaTrader5 as mt5
import pandas as pd
import talib as ta


class trader:
    def initiate():
        if mt5.initialize():
            return True
        else:
            return False

    def account_info():
        return mt5.account_info()

    def account_info_dict():
        return mt5.account_info()._asdict()

    def get_symbols(str):
        return mt5.symbols_get(str)

    def get_candles(symbol, tm, start, number):
        rates = mt5.copy_rates_from_pos(symbol, tm, start, number)
        rates_frame = pd.DataFrame(rates)
        return rates_frame

    def extend_columns(rates_frame):
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame['EMA_9'] = ta.EMA(rates_frame['close'], timeperiod = 9)
        rates_frame['EMA_20'] = ta.EMA(rates_frame['close'], timeperiod = 20)
        return rates_frame

