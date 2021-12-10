from os import X_OK


class BankAccount:
    # interest = .01
    balance = []
    bankName = "First Bank of Dojo"

    def __init__(self,intRate,balance,):
        self.intRate = intRate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw (self,amount):
        withdrawalAmount = amount
        self.balance -= withdrawalAmount
        print("New balance after withdraw :", self.balance)
        return self

# How can i add a $ sign to end of self.balance
    def displayAccountInfo(self):
        print("Current balance:", self.balance)
        return self
    
    def yieldInterest(self):
        print("Before interest", self.balance)
        x = self.balance * self.intRate
        self.balance += x
        print("After interest", self.balance)
        return self



alpha = BankAccount(.001, 100)
bravo = BankAccount(.001, 1000)

alpha.deposit(500).deposit(500).deposit(100).withdraw(400).yieldInterest().displayAccountInfo()
bravo.deposit(300).deposit(200).withdraw(100).withdraw(50).withdraw(50).withdraw(50).yieldInterest().displayAccountInfo()