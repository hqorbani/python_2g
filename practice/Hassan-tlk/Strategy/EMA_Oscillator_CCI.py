from trader import trader
import pandas as pd
import talib as ta
import MetaTrader5 as mt5

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

    def open_position(symbol_str="EURUSD_i", order_type="buy"):
        
        symbol = symbol_str
        lot = 0.01
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        
        risk_percent = 2
        # vvvvvvvvvv Calculate StopLost AND TakeProfit vvvvvvvvv
        order_type = order_type
        account_info_dict = __class__.get_account_info()
        free_margin = account_info_dict["margin_free"]
        from_, to = price - 100 * point, price + 100 * point
        for i in range(int(from_), int(price)):
            profit_calc = __class__.calc_profit(mt5.ORDER_TYPE_BUY , symbol , 0.01 , price, i)
            precent = profit_calc * (free_margin/100)
            if ((risk_percent + 0.2) >= precent >= (risk_percent - 0.2)) and order_type == "buy":
                sl = i

            profit_calc = __class__.calc_profit(mt5.ORDER_TYPE_SELL , symbol , 0.01 , price, i)
            precent = profit_calc * (free_margin/100)
            if ((risk_percent + 0.2) >= precent >= (risk_percent - 0.2)) and order_type == "sell":
                tp = i

        for i in range(int(price), int(to)):
            profit_calc = __class__.calc_profit(mt5.ORDER_TYPE_BUY , symbol , 0.01 , price, i)
            precent = profit_calc * (free_margin/100)
            if ((risk_percent + 0.2) >= precent >= (risk_percent - 0.2)) and order_type == "buy":
                tp = i

            profit_calc = __class__.calc_profit(mt5.ORDER_TYPE_SELL , symbol , 0.01 , price, i)
            precent = profit_calc * (free_margin/100)
            if ((risk_percent + 0.2) >= precent >= (risk_percent - 0.2)) and order_type == "sell":
                sl = i
        # ^^^^^^^ Calculate StopLost AND TakeProfit ^^^^^^^^^


        if order_type == "buy":
            order_type = mt5.ORDER_TYPE_BUY
        elif order_type == "sell":
            order_type = mt5.ORDER_TYPE_SELL
            
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        if StopLost:
            request.update({"sl":StopLost})
        if TakeProfit:
            request.update({"tp":TakeProfit})
        
        # send a trading request
        result = mt5.order_send(request)
        print(type(result))
        print(result)

    def shooting_star(rate_frame):
        # before candle:
        b_candle = rate_frame.iloc[-4]
        # current candle:
        c_candle = rate_frame.iloc[-3]
        # next candle:
        n_candle = rate_frame.iloc[-2]
        if ((b_candle.open < b_candle.close) and
        (n_candle.open > n_candle.close) and
        (c_candle.open > c_candle.close) and
        (c_candle.low < (c_candle.open - c_candle.close)) and
        (c_candle.high > ((70*(c_candle.open - c_candle.close))/100))):
            return True
    
    def calc_profit(action , symbol , volume , price_open, price_close):
        return mt5.order_calc_profit(action , symbol , volume , price_open, price_close)


