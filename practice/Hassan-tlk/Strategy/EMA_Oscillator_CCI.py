from trader import trader
import pandas as pd
import talib as ta

class EMA_Oscillator(trader):
    def extend_columns(rates_frame):
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        rates_frame['ema_8'] = ta.EMA(rates_frame['close'], timeperiod = 8)
        rates_frame['ema_28'] = ta.EMA(rates_frame['close'], timeperiod = 28)

        rates_frame['ociltr_CCI_30'] = ta.CCI(rates_frame['high'], rates_frame['low'], rates_frame['close'], timeperiod=30)
        
        return rates_frame

    #check for buy
    def ready_buy(rate_frame):
        if (((rate_frame.iloc[-3].ema_8 < rate_frame.iloc[-3].ema_28) and 
        (rate_frame.iloc[-2].ema_8 > rate_frame.iloc[-2].ema_28)) and
        rate_frame.iloc[-2].ociltr_CCI_30 > 0): 
            return True

    def ready_sell(rate_frame):
        if (((rate_frame.iloc[-3].ema_8 > rate_frame.iloc[-3].ema_28) and 
        (rate_frame.iloc[-2].ema_8 < rate_frame.iloc[-2].ema_28)) and
        rate_frame.iloc[-2].ociltr_CCI_30 < 0): 
            return True

    def open_position():
        symbol = "EURUSD_i"
        lot = 0.01
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            # "sl": price - 100 * point,
            # "tp": price + 100 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script [EMA_Oscillator] open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        
