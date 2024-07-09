from datetime import datetime

class AccountOpening:
    def __init__(self, accno, accdate, name, nominee, acctype, balance=0.0):
        self.accno = accno
        self.accdate = accdate
        self.name = name
        self.nominee = nominee
        self.acctype = acctype
        self.balance = balance

class Deposit:
    def __init__(self, tid, tdate, accno, damount):
        self.tid = tid
        self.tdate = tdate
        self.accno = accno
        self.damount = damount

class Withdraw:
    def __init__(self, tid, tdate, accno, wamount):
        self.tid = tid
        self.tdate = tdate
        self.accno = accno
        self.wamount = wamount

class BalanceEnquiry:
    def __init__(self, accno):
        self.accno = accno

class Bank:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def open_account(self):
        accno = int(input('Enter Account number:'))
        if accno in self.accounts:
            print("Account already exists!")
            return
        
        accdate = datetime.now()
        name = input('Enter your Name:')
        nominee = input('Enter name of the nominee:')
        acctype = input('Enter Account type:')
        
        account = AccountOpening(accno, accdate, name, nominee, acctype)
        self.accounts[accno] = account
        
        print("Account", accno, "opened successfully!")

    def deposit(self):
        tid = int(input('Enter Transaction ID:'))
        accno = int(input('Enter Account number:'))
        if accno in self.accounts:
            tdate = datetime.now()
            damount = float(input('Enter the amount to be deposited:'))
            deposit = Deposit(tid, tdate, accno, damount)
            self.transactions.append(deposit)
            self.accounts[accno].balance += damount
            print(f"Deposited {damount} to account {accno}")
        else:
            print("Account does not exist!")

    def withdraw(self):
        tid = int(input('Enter Transaction ID:'))
        accno = int(input('Enter Account number:'))
        if accno in self.accounts:
            wamount = float(input('Enter withdrawal amount:'))
            if self.accounts[accno].balance >= wamount:
                tdate = datetime.now()
                withdraw = Withdraw(tid, tdate, accno, wamount)
                self.transactions.append(withdraw)
                self.accounts[accno].balance -= wamount
                print(f"Withdrew {wamount} from account {accno}")
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist!")

    def balance_enquiry(self):
        accno = int(input('Enter Account number:'))
        if accno in self.accounts:
            balance = self.accounts[accno].balance
            print(f"Balance for account {accno}: {balance}")
        else:
            print("Account does not exist!")
    
    def menu(self):
        while True:
            print("\nBank Menu:")
            print("1. Open Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Balance Enquiry")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            
            match choice:
                case '1':
                    self.open_account()
                case '2':
                    self.deposit()
                case '3':
                    self.withdraw()
                case '4':
                    self.balance_enquiry()
                case '5':
                    print("Exiting...")
                    break


bank = Bank()
bank.menu()



