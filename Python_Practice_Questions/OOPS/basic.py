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


# Modeling a Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        
    def get_balance(self):
        return self.balance
    
# Creating an object of the BankAccount class
account1 = BankAccount("Alice", 1000)
print(account1.owner)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.get_balance())
print(account1.withdraw(1500))
print(account1)
    