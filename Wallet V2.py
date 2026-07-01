from datetime import datetime

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

     def get_balance(self):
          return self.balance
     
     def transfer(self, amount):
          if amount > self.balance:
               return"You don't have enough money to compelete this transaction"
                    
          self.balance -= amount
          self.history.append(f"{datetime.now()} - Tansfer -$ {amount}")


class Saving_account(Account):
     def __init__(self, owner, balance):
          super().__init__(owner)
          self.interest_rate = 0.03
         

     
     def transfer(self,amount):
         fee = amount * 0.0015
         total = fee + amount
         print("Bank transfer with small fee")


     
          


class Checking_account(Account):
     pass


class Credit_account(Account):
     def __init__(self,owner):
          super().__init__(owner)
          self.credit_amount = 20000
          self.bank_overdraft = 30000
          pass
          

class Crypto_account(Account):
     
     def transfer(self,amount):
          fee = amount * 0.02
          total = amount + fee
          print("Crypto transfer with fee")



def make_transfer(account):
     account.transfer()


savingAccount = Saving_account("Henger", 0)
checkingAccount = Checking_account()
creditAccount = Credit_account()
cryptoAccount = Crypto_account()


make_transfer(savingAccount)
make_transfer(checkingAccount)
make_transfer(creditAccount)
make_transfer(cryptoAccount)



while True:

     print("\nWelcome to your wallet, what do you want to do today?")
     print("balance, history, deposit, transfer")

     options = input("Choose an option: ")

     if options == "deposit":
          print(f"You Deposited {savingaccount.deposit(0)}")