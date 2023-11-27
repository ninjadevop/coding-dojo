class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts_info(cls, accounts):
        for account in accounts:
            print(
                f"Account Balance: ${account.balance}, Interest Rate: {account.interest_rate}"
            )
