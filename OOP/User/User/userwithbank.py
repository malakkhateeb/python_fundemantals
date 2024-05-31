class user:
    def __init__(self, name, initial_balance):
        self.userName = name
        self.bankAccount = Bankaccount(0.05, initial_balance)

    def deposit(self, amount):
        self.bankAccount.depositAmount(amount)
        return self

    def make_withdrawal(self, amount):
        self.bankAccount.withdrawAMount(amount)
        return self

    def display_user_balance(self):
        print(f"user: {self.userName}, Balance: {self.bankAccount.balance}")
        return self

    def transfer_money(self, other_user, amount):
        if self.bankAccount.balance >= amount:
            self.bankAccount.withdrawAMount(amount)
            other_user.bankAccount.depositAmount(amount)
            print(f"Transferred {amount} from {self.userName} to {other_user.userName}")
        else:
            print("Failed Transfer")
        return self, other_user
    def yield_interest(self):
        self.bankAccount.yield_interest()

class Bankaccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = balance

    def depositAmount(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"The Balance is: {self.balance}$")
        return self

    def withdrawAMount(self, amount):
        self.amount = amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
            print(f"Withdrawal of {self.amount}$ and the balance is: {self.balance}$")
        return self

    def display_account_info(self):
        print(f"The Balance: {self.balance}$")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate
            print (f"the final balance discounted rate {self.balance}")
        else:
            print("The Balance is 0$")

# Testing the classes
user1 = user("ahmed", 1000)
user2 = user("Ali", 5000)
user3 = user("yousef", 4000)

user1.deposit(200).deposit(100).deposit(50).make_withdrawal(700).display_user_balance()
user1.yield_interest()
user2.deposit(300).deposit(500).make_withdrawal(300).make_withdrawal(300).display_user_balance()
user3.deposit(100).make_withdrawal(200).make_withdrawal(100).make_withdrawal(500).display_user_balance()

user1.transfer_money(user3, 300)
user3.display_user_balance()
user1.display_user_balance()
