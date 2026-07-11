from time import time

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

         if total > self.balance:
              return "You don't have enough balance to transfer"
         self.balance -= total

         # Testing this line to see if it works, if not I will remove it and just use the self.balance -= total
         # Account.balance += amount

         return f"Transfer Completed, your new balance is {self.balance} and the fee was ${fee}"

     def withdraw (self,amount):
          
          if amount > self.balance:
               return "You don't have enough balance"
          
          elif amount < self.balance:
          
               self.balance -= amount

               
               return amount
               
          else:
               return "You can't withdraw 0 please, type right a amount to withdraw"

          
     def annual_interest_rate(self):
          

          if self.balance >= 10000:
               apply_interest = self.balance * self.interest_rate
               self.balance += apply_interest
               return self.balance
          else:
               return "You need a minimun deposit of $10,000 to apply the interest rate"
          
     def get_balance(self):
          return self.balance
     
     # Transacction history, withdraw and deposit history
     
     def history(self):
          return self.history
     
     withdraw_history = {
          "date": [datetime.now()],
          "amount": [(withdraw)]
     }
     deposit_history = {
          "date": [],
          "amount": []
     }

     transfer_history = {
          "date": [],
          "amount": [transfer]
     }

          


saving_account = Saving_account("Henger")

saving_account.deposit(30000)


print(f"your interest rate is {saving_account.annual_interest_rate()}")

print(saving_account.get_balance())

print(f"You withdrew -${saving_account.withdraw(100)}")

print(saving_account.get_balance())

print(saving_account.transfer(1000))

print(saving_account.withdraw_history, saving_account.deposit_history, saving_account.transfer_history)