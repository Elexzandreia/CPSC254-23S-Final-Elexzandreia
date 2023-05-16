class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.history = {'date':'info'} #dictionary with history info where date (in numbers) is the key and value is description
        self.balance = 0.0

    def withdrawal(self):
        amount = float(input("Enter withdrawal amount: "))
        self.balance -= amount
        print("Your new balance is:", self.balance)
    
    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        self.balance += amount
        print("Your new balance is:", self.balance)
        
    def check_balance(self):
        print("Your current balance is ", self.balance)
