class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self , lang):
        super().__init__()
        self.speaks.append(lang)


kid = Child("spanish")
print(len(kid.speaks))
print(kid.speaks)