class trader:
    
    def __init__(self , name , family , currency,profit , losses , buycurrency , currencysale) :
        self.name = name #property
        self.family = family #property
        self.currency = currency #property
        self.profit = profit #property
        self.losses = losses #property
        self.buycurrency = buycurrency #property
        self.currencysale = currencysale #property


    def introduce_yourself(self):
        return f"I'm {self.name} {self.family} and my currency is {self.currency}"
    def say_hello(self):
        return "Hello dear," 
