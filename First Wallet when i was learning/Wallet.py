from datetime import datetime

class Wallet():
        def __init__(self):
                self.balance = 0
                self.deposit_list = []
                self.transfer_list = []
        
        def deposit(self,amount,):
                if amount <=0:
                        print("Invalid balance, you can't deposit negative balance, please deposit the right amount")
                        return
                self.balance += amount
                self.deposit_list.append(("deposits",amount,datetime.now()))

        def check_balance(self):
                print(f"Your balance is", self.balance)


        def transfer(self,amount):
                
                if amount > self.balance:
                        print("You don't have enough money to compelete this transaction")
                        return
                
                self.balance -= amount

                self.transfer_list.append(("transfer", amount, datetime.now()))
        
        def history(self):
                print("\nDeposits")
                print("---------------------------------------------------")

                for op, amount, date in self.deposit_list:
                        print(f"{date} | +{amount}")

                print("\nTransfers")
                print("---------------------------------------------------")

                for op, amount, date in self.transfer_list:
                        print(f"{date} | -{amount}")
                


my_wallet = Wallet()

while True:

    print("Welcome to your wallet, what do you want to do today?")

    print("balance, history, deposit, transfer")

    options = input("Choose an option: ")


    if options == "deposit":
         
                deposit = int(input("Please type the amount you want to deposit: ")) 

                if deposit <= 0:
                        print("Invalid balance, you can't deposit negative balance, please depoist the right amount")

                else:
                        print ("You deposited", deposit)
                        my_wallet.deposit(deposit)



    elif options == "balance":
                    
                   my_wallet.check_balance()

    elif options == "transfer":
            transfer = int(input("How much do you want to transfer?: "))
            print (f"You Transfered: ", transfer)
            my_wallet.transfer(transfer)

    elif options == "history":
        
        my_wallet.history()
            

    elif options == "exit":
        break;
