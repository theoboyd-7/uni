class Customer:
     
    def __init__(self, name, membership_type):
        self.cust_name = name
        self.membership_type = membership_type

    def __str__(self):
        return f"Customer: {self.cust_name} ({self.membership_type} Member)"

class BankStatement:

    bank_name = "Global Bank"
    
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.__balance = balance
        self.owner = owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance > -100:
            self.__balance = new_balance
        else:
            print("Overdraft limit exceeded")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def __str__(self):
        return f"Bank Name: {self.bank_name} | Account: {self.account_number} | Balance: £{self.balance:.2f} | Owner: {self.owner.cust_name}"
    
def test():
    cust = Customer("Marcus", "Gold")
    bank_statement = BankStatement(1, 500, cust)

    print(cust)
    print(bank_statement)

    bank_statement.balance = -50
    print(bank_statement)

    bank_statement.balance = -1000
    print(bank_statement)

    bank_statement.deposit(1000)
    print(bank_statement)

test()