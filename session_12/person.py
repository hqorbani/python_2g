class person:
    def __init__(self , name , family) -> None:
        self.first_name = name
        self.last_name = family
    
    def introduce_your_self(self):
        return f"Hi , my name is {self.first_name} and my last name is {self.last_name}"
