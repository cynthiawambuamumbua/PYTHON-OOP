#  2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Car:
    color="blue"
    def __init__(self,owner,make,price):
     self.owner=owner
     self.make=make
     self.price=price
    def instatiate(car):
     car=Car()
    #  car=Car.owner="cynthia",make="Toyota",price=2.5 M
     return f"Car{Car.owner} {Car.make} {Car.price}"


