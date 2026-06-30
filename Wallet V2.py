class account:
     def __init__(self):
          self.balance = 0
          self.history = []
     
     def deposit(self,amount):
          self.balance += amount

     def get_balance(self):
          return self.balance


class saving_account(account):
     pass


class checking_account(account):
     pass


class crypto_account(account):
     pass


class credit_account(account):
     pass


while True:

     print("\nWelcome to your wallet, what do you want to do today?")
     print("balance, history, deposit, transfer")

     options = input("Choose an option: ")