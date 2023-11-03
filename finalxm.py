from abc import ABC, abstractmethod
import random

class Account(ABC):
    accounts={}
    transaction_history={}

    def __init__(self,name,email,address,accType):
        self.name =name
        self.email= email
        self.address= address
        self.accNo= random.randint(1000, 9999)
        self.accType=accType
        self.balance=0
        self.loan_taken=0
        self.loan_limit=2

    def deposit(self,amount):
        if amount >= 0:
            self.balance+=amount
            Account.transaction_history[self.accNo]=(f"Deposited ${amount}")
        else:
            print('Invalid amOunt')

    def withdraw(self,amount):
        if amount >=0 and amount<= self.balance:
            self.balance-= amount
            Account.transaction_history[self.accNo] =(f"Withdrew ${amount}")
        else:
            print('Withdrawal amount exceeded')
    def check_balance(self):
        print(f"Available Balance: ${self.balance}")

    def check_transaction_history(self):
        if self.accNo in Account.transaction_history:
            print("Transaction History:")
            for transaction in Account.transaction_history[self.accNo]:
                print(transaction)
    def take_loan(self, amount):
        if self.loan_limit>0:
            self.loan_taken+=amount
            self.balance+=amount
            self.loan_limit-=1
            Account.transaction_history[self.accNo] = (f"Took a Loan of ${amount}\nAfter taking  loan Main Balance: ${self.balance}")
        else:
            print("Unable to take a loan at this moment")
    def transfer(self,receiver_accNo,amount):
        if receiver_accNo in Account.accounts:
            receiver=Account.accounts[receiver_accNo]
            if amount<=self.balance:
                self.balance-=amount
                receiver.balance+=amount
                Account.transaction_history[self.accNo]=(f"Transferred ${amount} TO {receiver.name}\nAccount Number: {receiver.accNo}")
            else:
                print("Insufficient Balance for the transfer")
        else:
            print("Account does not exist")
    @abstractmethod
    def show_info(self):
        pass
class SavingsAccount(Account):
    def __init__(self,name,email,address):
        super().__init__(name,email,address,"Savings")

    def show_info(self):
        print(f"Account Type:{self.accType}")
        print(f"Name: {self.name}")
        print(f"Email:{self.email}")
        print(f"Account Number:{self.accNo}")
        print(f"Current Balance: ${self.balance}")

class CurrentAccount(Account):
    def __init__(self,name,email,address):
        super().__init__(name,email,address,"Current")

    def show_info(self):
        print(f"Account Type:{self.accType}")
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Account Number:{self.accNo}")
        print(f"Current Balace:${self.balance}")

class Admin:
    @staticmethod
    def create_account(name,email,address,accType):
        if accType.lower()=="savings":
            account=SavingsAccount(name,email,address)
        elif accType.lower()=="current":
            account=CurrentAccount(name,email,address)
        else:
            print("Invalid Account Type")
            return

        Account.accounts[account.accNo] = account
        print("Account created successfullyyyy!")
    @staticmethod
    def delete_account():
        accNo = int(input("Enter account number to delete: "))
        if accNo in Account.accounts:
            del Account.accounts[accNo]
            print("Account Deleted successfully")
        else:
            print("Account does not exist")
    @staticmethod
    def list_all_acc():
        for accNo,account in Account.accounts.items():
            print(f"Account Number: {accNo}")
            print(f"Name:{account.name}")
            print(f"Account Type:{account.accType}")
            print(f"Current Balance:${account.balance}")
            print()

    @staticmethod
    def total_bank_amnt():
        total_amnt=sum(account.balance for account in Account.accounts.values())
        print(f"Total Bank Balance: ${total_amnt}")
    @staticmethod
    def total_loan_amnt():
        total_loan=sum(account.loan_taken for account in Account.accounts.values())
        print(f"Total Loan Amount: ${total_loan}")

while True:
    print("1. User")
    print("2. Admin")
    print("3.Exit")
    user_ch =int(input("Select user type: "))
    if user_ch== 1:
        print("1.Create Account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check Balance")
        print("5.Check Transaction History")
        print("6.Take a Loan")
        print("7.Transfer Money")
        print("8. Exit")
        user_option=int(input("Select user option: "))

        if user_option ==1:
            name= input("Name: ")
            email= input("Email: ")
            address =input("Address: ")
            print("Account Types: ")
            print("1.Savings")
            print("2.Current")
            acc_type_choice=int(input("Select your account type: "))

            if acc_type_choice==1:
                accType="savings"
            elif acc_type_choice==2:
                accType="current"
            else:
                print("Invalid account type")
                continue

            Admin.create_account(name,email,address,accType)

        elif user_option == 2:
            accNo=int(input("Enter your account number: "))
            amount=float(input("Enter the deposit amount: "))
            if accNo in Account.accounts:
                account= Account.accounts[accNo]
                account.deposit(amount)
            else:
                print("Account does not exist")

        elif user_option==3:
            accNo =int(input("Enter your account number: "))
            amount = float(input("Enter the withdrawal amount: "))
            if accNo in Account.accounts:
                account= Account.accounts[accNo]
                account.withdraw(amount)
            else:
                print("Account does not exist")

        elif user_option== 4:
            accNo= int(input("Enter your account number: "))
            if accNo in Account.accounts:
                account= Account.accounts[accNo]
                account.check_balance()
            else:
                print("Account does not exist")

        elif user_option== 5:
            accNo= int(input("Enter your account number: "))
            if accNo in Account.accounts:
                account = Account.accounts[accNo]
                account.check_transaction_history()
            else:
                print("Account does not exist")

        elif user_option== 6:
            accNo =int(input("Enter your account number: "))
            amount =float(input("Enter the loan amount: "))
            if accNo in Account.accounts:
                account =Account.accounts[accNo]
                account.take_loan(amount)
            else:
                print("Account does not exist")

        elif user_option==7:
            accNo=int(input("Enter your account number: "))
            receiver_accNo =int(input("Enter the recipient's account number: "))
            amount= float(input("Enter the transfer amount: "))
            if accNo in Account.accounts and receiver_accNo in Account.accounts:
                account=Account.accounts[accNo]
                account.transfer(receiver_accNo,amount)
            else:
                print("Account does not exist")

        elif user_option==8:
            print("Exiting User Panel")

    elif user_ch==2:
        admin_pass="admin"
        password=input("Enter admin password: ")
        if password==admin_pass:
                name=input("Name: ")
                email=input("Email: ")
                address=input("Address: ")
                print("\n1. Create Account")
                print("\n2. Delete Account")
                print("\n3. List All Accounts")
                print("\n4. Total Bank Balance")
                print("\n5. Total Loan Amount")
                print("\n6. Exit")
                admin_option=int(input("Select admin option: "))

                if admin_option==1:
                    Admin.create_account(name,email,address)
                elif admin_option==2:
                    Admin.delete_account()
                elif admin_option==3:
                    Admin.list_all_acc()
                elif admin_option==4:
                    Admin.total_bank_amnt()
                elif admin_option==5:
                    Admin.total_loan_amnt()
                elif admin_option==6:
                    print("Successfully exit")
    elif user_ch==3:
        print("Exiting the system")
        break
    else:
        print("Invalid option")
       
    
     
            