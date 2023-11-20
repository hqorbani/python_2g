import MetaTrader5 as mt5
import pandas as pd
class trader:
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

    def get_candles(symbol , tm , start , number):
        # symbol , tm , start , number 
        # این متد قراره اطلاعات کندلی مربوط به 15 کندل اخیر را دریافت کند
        # ورودی های متد را خودتان مشخص کنید
        rates = mt5.copy_rates_from_pos(symbol , tm , start , number)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'] , unit= 's')
        rates_frame.drop('real_volume' , inplace = True , axis= 1)
        rates_frame.drop('tick_volume' , inplace = True , axis= 1)
        return rates_frame

    def open_position(symbol, p_type, lot):
        if p_type == "buy":
            p_type = mt5.ORDER_TYPE_BUY
        else:
            p_type = mt5.ORDER_TYPE_SELL

        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": p_type,
            "price": price,
            "sl": price - 100 * point,
            "tp": price + 100 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        
        # send a trading request
        result = mt5.order_send(request)
        print(type(result))
        print(result)
    
      



