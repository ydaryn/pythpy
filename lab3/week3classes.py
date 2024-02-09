#classes 
#ex1
class Str1ng:
    def __init__(self):
        self.input_string=""
    def getstr(self):
        self.input_string=input()
    def printUp(self):
        print(self.input_string.upper())

#ex2
class Shape:
    def __init__(self)
        pass
    def area(self)
        return 0
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
    def area(self):
        return length**2
    
#ex3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#ex4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def distance(self, sec_point):
        dx = self.x - sec_point.x
        dy = self.y - sec_point.y
        return (dx**2 + dy**2)**0.5
    
#ex5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"Replenished {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("May be negative balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")    
            
#ex6            
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#for example
numbers = [2, 3, 6, 7, 11, 14, 20]
prime_nums = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)
