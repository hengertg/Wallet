from account import *

class Credit_account(Account):
     def __init__(self,owner):
          super().__init__(owner)
          self.credit_amount = 20000
          self.bank_overdraft = 30000
          pass