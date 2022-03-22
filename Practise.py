# t = (1,2,3)
# print(t, type(t))

# t = (10)
# print(t, type(t)) # gives int class as single element is passed

# t = ('10')
# print(t, type(t)) # gives int class as single element is passed

# t = (10,)
# print(t, type(t)) # gives tuple class when single element is passed with comma

# t = tuple('Hello')
# print(t)

# t = tuple(input('Enter a string: '))
# print(type(t), t)

# t = eval(input('Enter a string: '))
# print(type(t), t)

# t = (1,2,3,4)
# for i in range(0,len(t)):
#     print(f'Index {i} and its value {t[i]}')

from xmlrpc.server import list_public_methods


t1 = (1,2,3)
t2 = (4,5,6)
t11 = (1.0,2.0,3.0)
t3 = t1+t2
# print(t3[:-1])
# print(t3[::-1])
# print(t3[::2])
# print(t1 == t11)

# a,b,c = t1
# print(a,b,c)

# del t1[1] # TypeError: 'tuple' object doesn't support item deletion
# del t11

# print(len(t1))
# print(max(t1))
# print(min(t1))
# print(t1.index(3))
# print(t1.count(3))
# t21 = tuple()
# t21 = tuple([1,2,3])
# t21 = tuple('123')
# t21 = tuple({'a':1,'b':2})
# print(t21)

# Ways to modify tuple content
# using Unpacking the tuple 
# t = (1,2,3)
# a,b,c = t
# b = '2'
# t = (a,b,c)
# print(t)

# Using list method
# t = (1,2,3)
# l = list(t)
# l[1] = '2'
# t = tuple(l)
# print(t)

# Program to print [2:6]
# t = ('T','H','GM','F','BMW','V','M','F','P')
# for i in range(2,7):
#     print(i,'\t',t[i])

