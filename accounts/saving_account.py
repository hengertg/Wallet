from account import *

class Saving_account(Account):
     def __init__(self, owner, balance):
          super().__init__(owner)
          self.interest_rate = 0.03
         

     
     def transfer(self,amount):
         fee = amount * 0.0015
         total = fee + amount
         print("Bank transfer with small fee")

     def withdraw (self,amount):
          self.withdraw -= amount
          if self.withdraw < 0:
               return "You can't withdraw 0 please, type right a amount to withdraw"