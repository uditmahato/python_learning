#class of bank account
class Bank_Account:
    __interest_rate=12
    __bank_name='Bank of Sunway'
    def __init__(self,first_name,last_name):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__balance=0
    def check_balance(self):
        print(f'Your balance is {self.__balance}')
    def deposit_balance(self,deposit_amt):
        if deposit_amt<0:
            print('Invalid amount')
        else:
            self.__balance+=deposit_amt
    def withdraw_balance(self,withdrawl_amt):
        if withdrawl_amt<0:
            print('Invalid amount')
        elif withdrawl_amt>self.__balance:
            print('Insufficient balance')
            print(f'Your balance is {self.__balance}')
        else:
            self.__balance-=withdrawl_amt
    @classmethod
    def get_interest_rate(cls):
        return cls.__interest_rate #get bank interest rate
    @classmethod
    def set_interest_rate(cls,new_rate):
        cls.__interest_rate=new_rate
    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name
    @staticmethod
    def print_holiday_list():
        print('Tihar Holiday')
# setting user_account to none initially
user_account=None
#Loop to run the program
while True:
    print('*************************************************************')
    print('Welcome to the {Bank_Account.get_bank_name()}')
    user_choice=input('Enter 1 to open bank account.\nEnter 2 to check balance.\nEnter 3 to deposit balance.\nEnter 4 to withdraw balance.\nEnter 5 to Get interest Rate.\nEnter 6 to change interest rate. \nEnter 7 to check holiday.\n')
    if user_choice =='1'and user_account is None:
        fn=input('Enter First Name : ')
        ln=input('Enter Last Name : ')
        user_account=Bank_Account(fn,ln)
        print('Congratulations! You have opened a bank account with us.')
    elif user_choice=='2' and user_account is not None:
        print('Your balance is {}'.format(user_account.__balance))
    elif user_choice=='3' and user_account is not None:
        balance=int(input('Enter deposit amount:  '))
        user_account.deposit_balance(balance)
        print('Deposit Successful')
        print('Your balance is {}'.format(user_account.__balance))
    elif user_choice=='4' and user_account is not None:
        withdraw=int(input('Enter the withdrawl amount : '))
        user_account.withdraw_balance(withdraw)
        print('Withdrawl Successful')
        print('Your balance is {}'.format(user_account.__balance))
    elif user_choice=='5' and user_account is not None:
        user_account.get_interest_rate()
        print('Interest Rate is {}'.format(user_account.get_interest_rate()))
    elif user_choice=='6' and user_account is not None:
        print('Warning: Changing interest rate will affect all bank accounts')
        new_rate=int(input('Enter the interest rate : '))
        Bank_Account.set_interest_rate(new_rate)
        print('Interest rate changed')
        print('Your New Interest Rate is {}'.format(Bank_Account.get_interest_rate()))
    elif user_choice=='7' and user_account is not None:
        Bank_Account.print_holiday_list()
    else:
        print("Print invalid input")
        