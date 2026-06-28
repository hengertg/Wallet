class Wallet:
        def __init__(self):
                self.Balance = 100000
        
        def deposit(self,amount):
                self.Balance += amount

        def check_balance(self):
                print(f"Your balance is", self.Balance)

        def transaction_history(self):
                pass 

        def transfer(self,amount):
                self.Balance -= amount
                

                


my_wallet = Wallet()

while True:

    print("Welcome to your wallet, what do you want to do today?")

    print("Balance, History, Deposit, Transfer")

    options = input("Choose an option: ")


    if options == "Deposit":
                    deposit = int(input("Please type the amount you want to deposit: "))
                    print ("You deposited", deposit)
                    my_wallet.deposit(deposit)



    elif options == "Balance":
                    
                   my_wallet.check_balance()

    elif options == "Transfer":
            transfer = int(input("How much do you want to transfer?: "))
            print (f"You Transfered: ", transfer)
            my_wallet.transfer(transfer)

    elif options == "History":
        pass
            

    elif options == "Exit":
        break;
