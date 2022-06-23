def add(a,b):
    print(f'The sum of {a} and{b} is {a+b}' )
def sub(a,b):
    if a>b:
        print(f'The subtraction {a} and {b} is {(a-b)}' )
    else:
        print(f'The subtraction {a} and {b} is {-1*(a-b)}' )
def mul(a,b):
    print(f'The multiplication of {a} and {b} is {a*b}')
def div(a,b):
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
    add(a,b)
        
elif o=='-':
    sub(a,b)  
elif o=='*':
    mul(a,b)
elif div=='/':
    div(a,b)
else:
    print('Invalid operator')
    

