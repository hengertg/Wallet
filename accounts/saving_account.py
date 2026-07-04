from account import *


# TO DO LIST FOR CLASS SAVING_ACCOUNT(ACCOUNT)

# Deposit ✅

# Withdraw ✅

# Transfer ⬜

# History ⬜

# Balance ⬜

# Annual Interest Rate ✅


class Saving_account(Account):
     def __init__(self, owner):
          super().__init__(owner)
          self.interest_rate = 0.015
         

     
     def transfer(self,amount):
         fee = amount * 0.0015
         total = fee + amount
         print("Bank transfer with small fee")

     def withdraw (self,amount):
          
          if amount > self.balance:
               return "You don't have enough balance"
          
          elif amount <= self.balance:
          
               self.balance -= amount

               
               return  amount
               
          else:
               return "You can't withdraw 0 please, type right a amount to withdraw"

          
     def annual_interest_rate(self):
          

          if self.balance >= 10000:
               apply_interest = self.balance * self.interest_rate
               self.balance += apply_interest
               return self.balance
          else:
               return "You need a minimun deposit of $10,000 to apply the interest rate"
          


saving_account = Saving_account("Henger")

saving_account.deposit(10000)


# print(f"your interest rate is {saving_account.annual_interest_rate()}")

print(saving_account.get_balance())

print(f"You withdrew -${saving_account.withdraw(100)}")

print(saving_account.get_balance())