class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Vehicle Move!")

  def stop(self):
    print("Vehicle stop")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Boat Sail!")
    
  def stop(self):
    print("Boat stop")

class Plane(Vehicle):
  def move(self):
    print("Plane Fly!")


car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

car1.move()
car1.stop()
boat1.move()
boat1.stop()



# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()