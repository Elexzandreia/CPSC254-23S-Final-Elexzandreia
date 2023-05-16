# has a member class/struct User that contains username & password & user activity history & balance information
# any other info/functions that you believe is necessary.
# can deposit/withdraw balance after login.

class User():
    def __init__(self, username, password, history, balance):
        self.username = username
        self.password = password

        self.history = {'date':'info'} #dictionary with history info where date (in numbers) is the key and value is description
        self.balance = balance

    def withdrawal(self):
        amount = float(input("Enter withdrawal amount: "))
        self.balance += amount
        print("Your new balance is:", self.balance)
    
    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.balance += amount
        print("Your new balance is:", self.balance)
        
    def balance(self):
        print("Your current balance is ", self.balance)
