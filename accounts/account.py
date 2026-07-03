import datetime

class Account:
     def __init__(self,owner):
          self.balance = 0
          self.history = []
          self.owner = owner
     
     def deposit(self, amount):
          if amount <=0:
               return "Invalid balance, you can't deposit negative balance, please deposit the right amount"
          
                        
          self.balance += amount
          self.history.append(f"{datetime.now()} - Deposit +$ {amount}")
          return "You deposit has been successful"

     def get_balance(self):
          return self.balance
     
     def transfer(self, amount):
          if amount > self.balance:
               return"You don't have enough money to compelete this transaction"
                    
          self.balance -= amount
          self.history.append(f"{datetime.now()} - Tansfer -$ {amount}")