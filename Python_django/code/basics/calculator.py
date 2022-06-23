# two input number
# operation
# add a+b
# sub a-b  neg to positive
# a/b
#the sum of

def calc(a,b,o):
    if o=='+':
        print(f'The sum of {a} and{b} is {a+b}' )
    elif o=='-':
        print(f'The subtraction {a} and{b} is {-1*(a+b)}' )
    elif o=='*':
        print(f'The multiplication of {a} and{b} is {a*b}')
    else:
        if a>b:
            print(f'The division of {a} by {b} is {a/b}' )
        else:
            print(f'The division of {b} by {a} is {b/a}' )
calc(int(input('Enter  the first number : ')),int(input('Enter  the second number : ')),input('Enter the operation : '))


