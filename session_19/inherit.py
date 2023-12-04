class Parent:
    hair_color = "brown"

class Child_1(Parent):
    pass

class Child_2(Parent):
    hair_color = "Black"

kid_1 = Child_1
kid_2 = Child_2

print(kid_1.hair_color)
print(kid_2.hair_color)