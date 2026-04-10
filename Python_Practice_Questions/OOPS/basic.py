# Defining Instance Varibales
class Employee:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#Creating an object of the class
emp1 = Employee("John", 30)
# print(emp1)
# print(emp1.name)
# print(emp1.age)


# Defining a class with Instance Methods
class Employee:
    # constructor 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"{self.name} is {self.age} years old."
        
# Creating an object of the class
# emp1 = Employee("John", 30)
# print(emp1)
# print(emp1.display())