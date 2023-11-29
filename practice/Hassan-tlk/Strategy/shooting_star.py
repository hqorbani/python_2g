import MetaTrader5 as mt5
import pandas as pd
import talib as ta
from EMA_Oscillator_CCI import EMA_Oscillator

class ShootingStar:
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
        rates = mt5.copy_rates_from_pos(symbole , tm , start , number)
        rates_frame_shtng_str = pd.DataFrame(rates)
        rates_frame_shtng_str.drop('real_volume' , inplace = True , axis= 1)
        rates_frame_shtng_str.drop('tick_volume' , inplace = True , axis= 1)
        return rates_frame_shtng_str

    def extend_columns(rates_frame_shtng_str):
        rates_frame_shtng_str['time'] = pd.to_datetime(rates_frame_shtng_str['time'] , unit= 's')
        rates_frame_shtng_str['shooting_star'] = ta.CDLSHOOTINGSTAR(rates_frame_shtng_str['open'], rates_frame_shtng_str['high'], rates_frame_shtng_str['low'], rates_frame_shtng_str['close'])
        return rates_frame_shtng_str

if __name__ == "__main__":
    shtng_str = ShootingStar
    ema_cci = EMA_Oscillator
    symbol  = "EURUSD_i"
    tm = 1 #mt5.TIMEFRAME_M30 # TIMEFRAME_H1
    start = 0
    number = 1500
    if shtng_str.connect():
        candle_shtng_str = shtng_str.get_candles(symbol , tm , start , number)
        frame_shtng_str = shtng_str.extend_columns(candle_shtng_str)
        for i in range(len(frame_shtng_str)):
            if frame_shtng_str.iloc[i].shooting_star != 0:
                print(frame_shtng_str.iloc[i].time, frame_shtng_str.iloc[i].shooting_star)
        # print(frame_shtng_str)