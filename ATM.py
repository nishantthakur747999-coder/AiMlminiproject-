class ATM:
    def __init__(self):
        self.balance=10000
        self.history=[]    
        
        
atm = ATM()  

while True:
            print("1.Check Balance")
            print("2. Deposit")
            print("3.Withraw")
            print("4. Transaction History")
            print("5.Exit")
            ch = int(input("Enter Choice:"))
            if ch == 1:
                print("Balance =",atm.balance)
            elif ch == 2:
                amount = int(input("Enter Deposit Amount:"))
                atm.balance += amount
                atm.history.append("Deposited"+str(amount))
                print ("Deposite Successful")
            elif ch == 3:
                amount = int(input("Enter Withdraw Amount:"))
                if amount <=atm.balance:
                    atm.balance -= amount
                    atm.history.append("Withdrawn" + str(amount))
                    print("Withdrawal Successful")
                else:
                    print("Insufficient Balance")
            elif ch == 4:
                print("Transaction History")
                for i in atm.history:
                    print(i)
            elif ch== 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice")