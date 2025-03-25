import json
import random

class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} says {self.sound}!"

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")
    
    def lay_egg(self):
        return f"{self.name} laid an egg."

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")
    
    def shear(self):
        return f"{self.name} has been sheared."

class Farm:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def list_animals(self):
        return [f"{animal.name} ({animal.__class__.__name__}, {animal.age} years old)" for animal in self.animals]

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(10000, 99999))
        while account_number in self.accounts:
            account_number = str(random.randint(10000, 99999))
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created. Number: {account_number}"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        return vars(account) if account else "Account not found."
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}
