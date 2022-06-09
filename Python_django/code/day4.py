#define tuple
tuple = (1,2,3,4,5,6,7,8,9,10)
print(tuple)

# heterogenious tuple
heterogenious_tuple = (1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h","i","j")
print(heterogenious_tuple)


#tuple properties

# tuple is indexed 

print(tuple[0])
print(tuple[-1])

#length of tuple
print(len(tuple))

#loop through tuple
for i in tuple:
    print(i)
#join tuple
print(tuple+heterogenious_tuple)   

#count in tuple
print(tuple.count(1))

#index in tuple
print(tuple.index(1))
