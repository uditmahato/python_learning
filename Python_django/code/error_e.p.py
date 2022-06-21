while True:
    try:
        a=int(input("Enter a number: "))
        b=int(input("Enter another number: "))
        print(a/b)
    except Exception as e:
        print(e)