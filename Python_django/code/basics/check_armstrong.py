#write  a program to check the number is armstrong or not
def check_armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if n==sum:
        return True
    else:
        return False
print(check_armstrong(153))
