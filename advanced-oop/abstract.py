from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    def description(self):
        pass


class Car(Vehicle):

    def go(self):
        return 'You drive a car!'

    def description(self):
        return 'This is a car!'
    

class Motorcycle(Vehicle):

    def go(self):
        return 'You drive a motorcycle!'

    def description(self):
        return 'This is a motorcycle!'
    

# v = Vehicle()
c = Car()
m = Motorcycle()

# print(v.go())
print(c.go())
print(m.go())