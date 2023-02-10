

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance >= 0:
            self.balance -= amount
        else:
            print("insufficient funds: charging a $5 fee")
        self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self
        # your code here
    def yield_interest(self):
        if self.balance > 0: 
            self.balance += (self.balance * self.int_rate)
        return self


savings = BankAccount(.05,5000)
checking = BankAccount(.03,3000)

(
    savings.deposit(1500)
        .deposit(500)
        .deposit(1300)
        .withdraw(800)
        .yield_interest()
        .display_account_info()
)

(
    checking.deposit(3500)
        .deposit(2000)
        .deposit(2300)
        .withdraw(1200)
        .yield_interest()
        .display_account_info()
)

# Create a User class with an __init__ method
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.03, balance=0)
    
    # other methods
    
    

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.withdraw(amount)
        return self


# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self


# Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        self.account.display_account_info()
        return self

