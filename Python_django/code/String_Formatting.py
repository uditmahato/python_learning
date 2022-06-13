#String formating is a way to format strings in python.

#example 1
name = "John"
age = 23
print("Hello %s. You are %d years old." % (name, age))

# string formatting using curly braces
print(f"Hello {name} .You are {age} years old")

#another way using .format
print("Hello {} .You are {} years old".format(name,age))