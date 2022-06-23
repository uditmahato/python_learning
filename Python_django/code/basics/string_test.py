a='Sis'
b='ter'
c=' is awesome'
#string concatenation
print(a+b)

#string concatenation  with space
print(a+' '+b)

print(a+b+c)

#delete  first name
del c
# print(c)
# c=' is awesome'

#len
print(len('is awesome'))

#string check
print('s' in a)

#use of not while checking
print('not s' in a)

#upper and lower in string
print(a.upper())
print(a.lower())

#capitalize
print(a.capitalize())

#replace
print(a.replace('is','is not'))

#decision tree algorithm
d='aeroplane'
print(d.split(' ')) #split string into list
print(d.split(' ')[0]) #get first element of list


#string strip
a='is aero this planet        '     #strip space remover
print(len(a))
print(len(a.strip()))


#string indexing
print(a[0])
print(a[1])

#string slicing
print(a[0:5])  #first element is inclusive and second is exclusive
print(a[0:6])

#string slicing with negative index
print(a[-1])
print(a[-2])

#string slicing with step
print(a[0:6:2])
print(a[0:6:3])

#string slicing with colon
print(a[:])


