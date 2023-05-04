# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
            #  - show_full_name
            #  - year_of_birth
            #  - show_initials

class Student:
    first_name="cynthia"
    last_name="mumbua"
    age=19
    country="kenya"

def __init__(self,show_full_name,year_of_birth,show_initials):
    self.show_full_name=show_full_name+self.last_name
    self.year_of_birth=year_of_birth
    self.show_initials=show_initials

student=Student()
print('Student:',student.first_name)
print('Student:',student.last_name)
print(f"Student:{student.first_name} {student.last_name}")
def show_initials(full_name):
    if (len(full_name) == 0):
      return
   
    show_initials = ''.join([name[0].upper()+"." for name in full_name.split(' ')])
    return show_initials
                
full_name="cynthia mumbua"
print(f"show_initials: {show_initials(full_name)}")


def year_of_birth(year_of_birth):
  current_year= 2023
age=19
year_of_birth =year_of_birth.current_year-age
print(f"Student:{year_of_birth.current_year}-{year_of_birth.age}")
print(f"Student:Hello,my name is {full_name},i am {age} years old,({show_initials})")



# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.



