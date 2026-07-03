from account import *

class Crypto_account(Account):
     
     def transfer(self,amount):
          fee = amount * 0.02
          total = amount + fee
          print("Crypto transfer with fee")
          pass