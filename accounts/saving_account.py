from account import *


# TO DO LIST FOR CLASS SAVING_ACCOUNT(ACCOUNT)

# Deposit ✅

# Withdraw ⬜

# Transfer ⬜

# History ⬜

# Balance ⬜

# Annual Interest rate calculator ✅


class Saving_account(Account):
     def __init__(self, owner):
          super().__init__(owner)
          self.interest_rate = 0.015
         

     
     def transfer(self,amount):
         fee = amount * 0.0015
         total = fee + amount
         print("Bank transfer with small fee")

     def withdraw (self,amount):
          self.withdraw -= amount
          if self.withdraw < 0:
               return "You can't withdraw 0 please, type right a amount to withdraw"
          
     def annual_interest_rate(self):
          

          if self.balance > 0:
               interest_rate_calc = self.balance * self.interest_rate
               self.balance += interest_rate_calc 
               return self.balance
          


saving_account = Saving_account("Henger")

saving_account.deposit(20000)

print(f"your interest rate is {saving_account.annual_interest_rate()}")