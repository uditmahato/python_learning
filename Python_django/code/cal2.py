
def add():
    print(f'The sum of {a} and{b} is {a+b}' )
def sub():
    if a>b:
        print(f'The subtraction {a} and {b} is {(a-b)}' )
    else:
        print(f'The subtraction {a} and {b} is {-1*(a-b)}' )
def mul():
    print(f'The multiplication of {a} and {b} is {a*b}')
def div():
    if a>b:
        print(f'The division of {a} by {b} is {a/b}' )
    else:
        print(f'The division of {b} by {a} is {b/a}' )

#take input from user
a=int(input('Enter  the first number : '))
b=int(input('Enter  the second number : '))
o=input('Enter the operation : ')

# select the operator to perform task

if o=='+':
    add()
        
elif o=='-':
    sub()  
elif o=='*':
    mul()
elif div=='/':
    div()
else:
    print('Invalid operator')
    

