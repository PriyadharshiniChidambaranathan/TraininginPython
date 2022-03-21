#  Define a property that must have the same value for every class instance (object)
#  Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.



----------------------------------------------------------


class Vehicle:
    color="white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


School_bus= Bus('volvo' , 30, 20)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car= Car('audii', 80 , 90)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)



-------------------------------
#       Output:
#         white volvo Speed: 30 Mileage: 20
#         white audii Speed: 80 Mileage: 90
