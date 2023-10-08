import MetaTrader5 as MT5
class trader:
    
    # def __init__(self , profit , lose , buy , sell) :
        
    #     self.profit = profit 
    #     self.lose = lose 
    #     self.buy = buy 
    #     self.sell = sell

    # def buy_bit(self):
    #     pass 
        
    # def profit_bit(self):
    #     pass
      def connect():
            if mt5.initialize():
                  return True
            else:
                  return False
      def get_price_list(symbol,timef):
            
            return mt5 .price_list(symbol , timef)
      def ma (symbol , timf ):
          price_list = get_price_list(symbol , timef)
          for i in price_list:
                i=0
           moving_average = []
          
