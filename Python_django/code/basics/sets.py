#Sets is    
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

#set properties
#------------------


#set is mutable
#set is unordered
#set is indexed
#set is iterable
#set is sequence
# set is heterogenous


# create set in python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = {1,2,3,4,5,6,7,8,9,10}

print(set3)

# access item in set
for x in set3:
    print(x)

#add items in set
set3.add(11)
print(set3)

#Join sets
set4 = set1.union(set2)
print(set4)

#Remove set items
set4.remove(4)
print(set4)

# pop items in set
set4.pop()
print(set4)

#clear  
set4.clear()
print(set4)
