a=list(range(1, 11))
even=[]
odd=[]
print(a)
# check if the elements of  list are oddd or even
def classify():
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Even numbers are:",even)
    print("odd numbers are:",odd)
classify()