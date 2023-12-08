from trader import Trader
class Pattern_recog(Trader):
    # def __init__(self) -> None:
    #     super().__init__()
    
    def shooting_star(rate_frame, n=0):
        # before candle:
        b_candle = rate_frame.iloc[n-4]
        # current candle:
        c_candle = rate_frame.iloc[n-3]
        # next candle:
        n_candle = rate_frame.iloc[n-2]
        if ((b_candle.open < b_candle.close) and
        (n_candle.open > n_candle.close) and
        (c_candle.open > c_candle.close) and
        (c_candle.low < (c_candle.open - c_candle.close)) and
        (c_candle.high > ((70*(c_candle.open - c_candle.close))/100))):
            return True

    def morning_star(rate_frame):
        # before candle:
        b_candle = rate_frame.iloc[-4]
        # current candle:
        c_candle = rate_frame.iloc[-3]
        # next candle:
        n_candle = rate_frame.iloc[-2]
        if (
            # check bearish
            b_candle.close < b_candle.open and
            # check bullish
            c_candle.close > c_candle.open and
            # check bullish
            n_candle.close > n_candle.open and
            
            c_candle.close < n_candle.open and
            c_candle.close < b_candle.close
        ):
            return True
    