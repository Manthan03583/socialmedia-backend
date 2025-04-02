
def add(num1: int, num2: int):
    sum = num1 + num2
    return sum

def subtract(num1: int, num2: int):
    sum = num1 - num2
    return sum

def multipy(num1: int, num2: int):
    sum = num1 * num2
    return sum

def divide(num1: int, num2: int):
    sum = num1 / num2
    return sum

class InsufficientFund(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance = 0):
        self.balance = starting_balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFund("Insufficient funds in account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *=1.1
    