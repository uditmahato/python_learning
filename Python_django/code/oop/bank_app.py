class Bank_Account:
    def __init__(self,first_name,last_name,balance):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__balance=0
  
    def check_balance(self):
        print(f'Your balance is {Self.__balance}')
    def deposit_balance(self,deposit_amt):
        self.__balance+=deposit_amt
    def withdraw_balance(self,withdrawl_amt):
        self.__balance-=withdrawl_amt
    @classmethod
    def get_interest_rate(cls):
        return cls.__interest_rate #get bank interest rate
    @classmethod
    def set_interest_rate(cls):
        pass
    @staticmethod
    def print_holiday_list():
        print('Tihar Holiday')
user_account=None
while True:
    user_choice=input('Enter 1 to open bank account.\nEnter 2 to  check balance..\n Enter 3 to deposit balance. \n Enter 4 to withdraw balance.\n Enter 5 to Get interest Rate.\n Enter 6 to change interest rate. \n  Enter 7 to check holiday ')
    if user_choice ==1:
        fn=input('Enter First Name : ')
        ln=input('Enter Last Name : ')
        user_account=Bank_Account(fn,ln)
    elif user_choice==2:
        user_account.check_balance()
    elif user_choice==3:
        balance=input('Enter deposit amount:  ')
        user_account.deposit_balance(balance)
    elif user_choice==4:
        withdraw=input('Enter the withdrawl amount : ')
        user_account.withdraw_balance(withdraw)
    elif user_choice==5:
        user_account.get_interest_rate()
    elif user_choice==6:
        pass
    elif user_choice==7:
        Bank_Account.print_holiday_list()
    else:
        print("Print invalid input")
        
