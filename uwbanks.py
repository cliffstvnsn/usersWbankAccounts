class BankAccount:
    def __init__(self, int_rate = .01, balance = 121): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self



class User:
    def __init__(self, name , email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name, self.email)
        self.account.display_account_info()
        return self

myUser1 = User("Andrew Stevenson", "clifford.andrew.stevenson@gmail.com")
myUser1.make_deposit(150).make_withdrawal(200).display_user_balance()



