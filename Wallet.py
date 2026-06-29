class Wallet:
        def __init__(self):
                self.Balance = 100000
                self.deposit_list = []
                self.transfer_list = []
        
        def deposit(self,amount):
                self.Balance += amount
                self.deposit_list.append(amount)

        def check_balance(self):
                print(f"Your balance is", self.Balance)


        def transfer(self,amount):
                self.Balance -= amount
                self.transfer_list.append(amount)
        
        def history(self):
                
                print("\nDeposits" )
                print("---------------------------------------------------")
                print(self.deposit_list)

                print("\nTransfers" )
                print("---------------------------------------------------")
                print(self.transfer_list)
                


my_wallet = Wallet()

while True:

    print("Welcome to your wallet, what do you want to do today?")

    print("balance, history, deposit, transfer")

    options = input("Choose an option: ")


    if options == "deposit":
                    deposit = int(input("Please type the amount you want to deposit: "))
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
