class person:
    #magic methods
    def __init__(self , name , family , mobile , color) :
        self.name = name #property
        self.family = family #property
        self.mobile = mobile #property
        self.color = color #property
        
    def introduce_yourself(self):
        return f"I'm {self.name} {self.family} and my mobile is {self.mobile}"
    def say_hello(self):
        return "Hello dear," + self.color