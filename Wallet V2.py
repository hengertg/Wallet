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
          return "You deposit has been successful"

     def get_balance(self):
          return self.balance
     
     def transfer(self, amount):
          if amount > self.balance:
               return"You don't have enough money to compelete this transaction"
                    
          self.balance -= amount
          self.history.append(f"{datetime.now()} - Tansfer -$ {amount}")



# TO DO LIST FOR CLASS SAVING_ACCOUNT(ACCOUNT)

# Deposit ✅

# Withdraw ⬜

# Transfer ⬜

# History ⬜

# Balance ⬜


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
          pass



# def make_transfer(account):
#     account.transfer()


# checkingAccount = Checking_account()
# creditAccount = Credit_account()
# cryptoAccount = Crypto_account()


# make_transfer(savingAccount)


# TO DO LIST FOR MENU

# Principal Menu ✅

# Saving Account Menu⬜

# Checking Account Menu ⬜

# Credit Account Menu ⬜

# Crypto Account Menut ⬜

while True:

     print("\nWelcome to your wallet, what do you want to do today?")
     print("Type the account you want to choose")
     print("Saving Account, Checking Account, Credit Account, Crypto Account, Go Back: to go to previous menu")

     user_options = input("Choose an option: ")



     if user_options == "Saving Account":
          savingAccount = Saving_account("Henger", 0)
          while True:

               print ("What do you want to do?")
               print("Deposit, Transfer, Withdraw, history or if you want to go back to previus menu pleease type Go back")
               saving_options = input("Type an option: ")

               if saving_options == "Deposit":

                    deposit_amount= int(input("Please type how much you want to deposit: "))
                    print(f"You Deposited {savingAccount.deposit(deposit_amount)}")

               if saving_options == "Go back":
                    break
                         
               
     elif user_options == "Exit":
          break