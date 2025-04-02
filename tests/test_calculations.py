# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from app.calculations import add, subtract, multipy, divide, BankAccount, InsufficientFund

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 26, 29),
    (4, 19, 23),
    (5, 10, 15),
    (6, 7, 13)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected
    
def test_subtract():
    print("testing subtract function")
    assert subtract(13, 8) == 5

def test_muliply():
    print("testing multipy function")
    assert multipy(5, 8) == 40

def test_divide():
    print("testing divide function")
    assert divide(10, 5) == 2

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (300, 160, 140),
    (400, 190, 210),
    (500, 100, 400),
    (600, 350, 250)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFund):
        bank_account.withdraw(200)