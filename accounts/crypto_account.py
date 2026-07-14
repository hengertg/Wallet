from account import *

class Crypto_account(Account):
     
     def transfer(self,amount):
          fee = amount * 0.02
          total = amount + fee
          print("Crypto transfer with fee")

          if total > self.balance:
               return "You don't have enough balance to transfer"
          
          elif amount <self.balance:

               amount -= self.balance
               return f"Transfer Completed, your new balance is {self.balance} and the fee was ${fee}"
     
     def withdraw_crypto(self, amount):
     
          
          if amount > self.balance:
               return f"You don't have enough balance"
          
          elif amount < self.balance:
          
               self.balance -= amount

               
               return amount
          
          else:
               return "Invalid balance, Please try again"
          ...