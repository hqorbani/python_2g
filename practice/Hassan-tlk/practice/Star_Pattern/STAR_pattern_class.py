# from trader import trader
import pandas as pd
import talib as ta
import MetaTrader5 as mt5

class StarPattern:
    # def __init__(self, username) -> None:
    #     self.username = username
    def connect():
        if mt5.initialize():
            return True
        else:
            return False
        
    def get_account_info():
        return mt5.account_info()._asdict()
    
    def get_symbols(str_symbols):
        return mt5.symbols_get(str_symbols)

    def get_candles(symbole , tm , start , number):
        # symbole , tm , start , number 
        # این متد قراره اطلاعات کندلی مربوط به 15 کندل اخیر را دریافت کند
        # ورودی های متد را خودتان مشخص کنید
        rates = mt5.copy_rates_from_pos(symbole , tm , start , number)
        rates_frame = pd.DataFrame(rates)
        rates_frame.drop('real_volume' , inplace = True , axis= 1)
        rates_frame.drop('tick_volume' , inplace = True , axis= 1)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        return rates_frame

    def morning_star(rate_frame):
        if ((rate_frame.iloc[-8].close > rate_frame.iloc[-7].close and
        rate_frame.iloc[-7].close > rate_frame.iloc[-6].close and
        rate_frame.iloc[-6].close > rate_frame.iloc[-5].close and
        rate_frame.iloc[-5].close > rate_frame.iloc[-4].close) and
        rate_frame.iloc[-4].open > rate_frame.iloc[-3].close and
        rate_frame.iloc[-3].close < rate_frame.iloc[-2].open and
        rate_frame.iloc[-2].open < rate_frame.iloc[-1].open):
            return True

    def evening_star(rate_frame):
        if ((rate_frame.iloc[-8].open < rate_frame.iloc[-7].open and
        rate_frame.iloc[-7].open < rate_frame.iloc[-6].open and
        rate_frame.iloc[-6].open < rate_frame.iloc[-5].open and
        rate_frame.iloc[-5].open < rate_frame.iloc[-4].open) and
        rate_frame.iloc[-4].close > rate_frame.iloc[-3].close and
        rate_frame.iloc[-3].close > rate_frame.iloc[-2].open and
        rate_frame.iloc[-2].open > rate_frame.iloc[-1].open):
            return True

    def morning_star_back_test(n, rate_frame):

        for i in range(8, n-8):
            if ((rate_frame.iloc[i-8].close > rate_frame.iloc[i-7].close and
            rate_frame.iloc[i-7].close > rate_frame.iloc[i-6].close and
            rate_frame.iloc[i-6].close > rate_frame.iloc[i-5].close and
            rate_frame.iloc[i-5].close > rate_frame.iloc[i-4].close) and
            rate_frame.iloc[i-4].open > rate_frame.iloc[i-3].close and
            rate_frame.iloc[i-3].close < rate_frame.iloc[i-2].open and
            rate_frame.iloc[i-2].open < rate_frame.iloc[i-1].open):
                print(candles.iloc[i-4].time, ":", candles.iloc[i-4].close)

if __name__ == "__main__":
    backtest = StarPattern
    if backtest.connect():

        symbole  = "EURUSD_i"
        tm = mt5.TIMEFRAME_M30 # TIMEFRAME_H1
        start = 0
        number = 1500
        candles = backtest.get_candles(symbole , tm , start , number)
        backtest.morning_star_back_test(number, candles)
