class Emplyee:
    # magic methods
    def __init__(self , name , age) -> None:
        self.name = name
        self.age = age
    
    def introduce_yourself(self):
        return f"my name is {self.name}"
    # magic methods
    def __str__(self) -> str:
        return "this is Emplyee class"

    def say_hello(self , message):
        return f"Hello {message}"

# karmand = Emplyee("Hamzeh" , 39)
# monshi = Emplyee("Hamzeh" , 39)
# print(karmand)
# print(karmand.introduce_yourself())

# if karmand == monshi:
#     print(True)
# else: 
#     print(False)
karmand = Emplyee("Hamzeh" , 39)

print(karmand.say_hello("How are you?"))
