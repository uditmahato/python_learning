#Type casting

#str to int
print(int("10"))
print(int("11"))

#str to float
print(float("10"))
print(float("10.5"))

#float to int
print(int(10.5))
print(int(10))

#int to str
print(str(10))
print(str(10.5))

#str to bool
print(bool("True"))
print(bool("False"))
print(bool(" "))

#int to bool
print(bool(10))
print(bool(0))
print(bool(-1))

#List
#list is a collection of items
#list is mutable
#list is ordered
#list is indexed
#list is iterable
#list is sequence

#list creation
d=[1,'a',2.5,'b',True]


#list index
print(d[0])
print(d[1])
print(d[2])

#list slicing
print(d[0:3])

#list slicing with negative index
print(d[-1])
print(d[-2])

#list slicing with step
print(d[0:6:2])
print(d[0:6:3])

#functions of list
#append
d.append(10)
print(d)

#del
del d[0]
print(d)

#insert
d.insert(0,10)  #edge case of insert
print(d)

#remove
d.remove(10)
print(d)

#pop
d.pop()
print(d)

#pop with index
d.pop(0)
print(d)

#copy
d1=d.copy()
print(d1)

#clear
d1.clear()
print(d1)

#len of list
print(len(d1))

#check if element is in the list
print(10 in d1)
print(10 not in d1)

#reate new list 
d2=list(range(1,10))
print(d2)

#reverse list
d2.reverse()
print(d2)

#sort list
d2.sort()
print(d2)

#sort list in reverse order
d2.sort(reverse=True)
print(d2)
