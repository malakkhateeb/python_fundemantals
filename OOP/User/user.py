class user:
    def __init__(self,name,balance):
        self.userName=name
        self.accountbalance=balance
        # deposit amount to balance
    def deposit(self,amount):
        self.amount=amount
        self.accountbalance +=amount
        print(f"{self.userName} deposit {self.amount} to Bank account and the balance is {self.accountbalance}")
        return self
# make withdrawal from balance 
    def make_withdrawal(self,amount):
        self.amount=amount
        if self.accountbalance >= amount:
            self.accountbalance -=amount
            print(f"withdrawal {amount} from {self.userName} Bank account and the balance is {self.accountbalance}")
        else:
            print("Failed Withdrawal")
        return self
# display the balance of the users 
    def display_user_balance(self):
        print(f"user:{self.userName},Balance: {self.accountbalance}")
        return self
# transfer amount from balance
    def transfer_money(self, other_user, amount):
        self.other_user=other_user
        self.amount=amount
        if self.accountbalance >= amount:
            self.accountbalance -= amount
            other_user.accountbalance += amount
            print(f"Transferred {amount} from {self.userName} to {other_user.userName}")
        else:
            print("Failed Transfer")
        return self, other_user
        
        

user1 = user("ahmed", 1000)
user2=user("Ali",5000)
user3=user("yousef", 4000)


user1.deposit(200)
user1.deposit(100)
user1.deposit(50)
user1.make_withdrawal(700)
user1.display_user_balance()



user2.deposit(300)
user2.deposit(500)
user2.make_withdrawal(300)
user2.make_withdrawal(300)
user2.display_user_balance()



user3.deposit(100)
user3.make_withdrawal(200)
user3.make_withdrawal(100)
user3.make_withdrawal(500)
user3.display_user_balance()



user1.transfer_money(user3,300)
user3.display_user_balance()
user1.display_user_balance()






