#break in python
#break is used to exit a loop.
# break example
for i in range(10):
    if i == 5:
        break
    print(i)
print("Done")

#continue in python
#continue is used to skip the current iteration and continue with the next iteration.
# continue example
for i in range(10):
    if i == 5:
        continue
    print(i)
print("Done")

# else in for loop
# else is used to execute a block of code when the loop is finished.
# else example
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("Done")
    