class Bankaccount:
    def __init__(self,int_rate,balance):
        self.rate = int_rate
        self.balance=balance

    def depositAmount(self,amount):
        self.amount=amount
        self.balance += amount
        print(f"the Balance is :{self.balance}$")
        return self
    
    def withdrawAMount(self,amount):
        self.amount=amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -=amount
            print(f"withdraw {self.amount}$ and the balance is : {self.balance}$")
        return self
    
    def display_account_info(self):
        print(f" the Balance : {self.balance}$")
        return self
    
    def yield_interest(self):
        if self.balance > 0 :
            self.balance = self.balance * self.rate
        else:
            print("the Balance is 0$")

first_account= Bankaccount( 70 , 1000)
second_account= Bankaccount(90, 2000)

first_account.depositAmount(100).depositAmount(200).depositAmount(400)
first_account.withdrawAMount(500).yield_interest().display_account_info()


second_account.depositAmount(100).depositAmount(300).withdrawAMount(200).withdrawAMount(100)
second_account.withdrawAMount(300).withdrawAMount(50).yield_interest().display_account_info()
