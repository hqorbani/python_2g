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
        rates_frame['EMA_9'] = ta.EMA(rates_frame['close'], timeperiod=9)
        rates_frame['slowk_335'], rates_frame['slowd_335'] = ta.STOCH(
            rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        rates_frame['slowk_3314'], rates_frame['slowd_3314'] = ta.STOCH(
            rates_frame['high'], rates_frame['low'], rates_frame['close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        return rates_frame

    # def check_buy(rate_frame):
    #     if (rate_frame.iloc[-1].slowk_335 > 20 and
    #         rate_frame.iloc[-1].slowk_3314 > 20 and
    #         rate_frame.iloc[-2].slowk_335 < 20 and
    #         rate_frame.iloc[-2].slowk_3314 < 20 and
    #             rate_frame.iloc[-1].low > rate_frame[-1].ema_9):
    #         return True

    # def check_sell(rate_frame):
    #     if (rate_frame.iloc[-1].slowk_335 < 80 and
    #         rate_frame.iloc[-1].slowk_3314 < 80 and
    #         rate_frame.iloc[-2].slowk_335 > 80 and
    #         rate_frame.iloc[-2].slowk_3314 > 80 and
    #             rate_frame.iloc[-1].high < rate_frame[-1].ema_9):
    #         return True
