# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Fruit:
    shape= "oval"
    def __init__(self, color, texture,flavor):
        self.color = color
        self.texture= texture
        self.flavor = flavor
    def my_fruit(self):
        my_fruit=Fruit()
        color="yellow"
        texture="smooth"
        flavor="sweet"
        print(f"i enjoy {color} mango {my_fruit} because it is {texture} and {flavor}?")