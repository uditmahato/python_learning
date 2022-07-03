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
    print('*************************************************************')
    print('Welcome to the {bank_name}')
    user_choice=input('Enter 1 to open bank account.\nEnter 2 to check balance.\nEnter 3 to deposit balance.\nEnter 4 to withdraw balance.\nEnter 5 to Get interest Rate.\nEnter 6 to change interest rate. \nEnter 7 to check holiday.\n')
    if user_choice =='1':
        fn=input('Enter First Name : ')
        ln=input('Enter Last Name : ')
        user_account=Bank_Account(fn,ln)
        print('Congratulations! You have opened a bank account with us.')
    elif user_choice=='2':
        user_account.check_balance()
    elif user_choice=='3':
        balance=int(input('Enter deposit amount:  '))
        user_account.deposit_balance(balance)
    elif user_choice=='4':
        withdraw=int(input('Enter the withdrawl amount : '))
        user_account.withdraw_balance(withdraw)
    elif user_choice=='5':
        user_account.get_interest_rate()
    elif user_choice=='6':
        pass
    elif user_choice=='7':
        Bank_Account.print_holiday_list()
    else:
        print("Print invalid input")
        