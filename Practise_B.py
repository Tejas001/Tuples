# If a is [1, 2, 3]
# al = [1,2,3]
# a = (1,2,3)
# print(a * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(a,a,a) # (1, 2, 3) (1, 2, 3) (1, 2, 3)
# print(a+a+a) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# al[1:1] = [1] # works in list 
# al[1:1] = 1 # do not work in list
# print(a[1:1]) # ()

# Slicing
# a = (1,2,3,4,5)
# print(a[1:3])

# a=('a')
# print(a, type(a)) # a <class 'str'>

# t = 3,4,5
# t1 = (3,4,5)
# print(t,t1) # (3, 4, 5) (3, 4, 5)

# t = (3,4,5)
# t1 = ((3,4,5))
# print(t,t1) # (3, 4, 5) (3, 4, 5)

# Empty tuple
# a = ()
# a1 = tuple()
# print(a,a1) # () ()

# tuple with one element
# a = (1,)
# print(a) # (1,)

# a= ('p','y','t','h','o')
# b =('n',)
# print (a+b)

# Diff between (30) and (30,)
# a = (30)
# a1 = (30,)
# print(a,a1) # 30 (30,)

# Program to find O/P
# plane = ('passenger','luggage')
# plane[1] = 'snakes' # TypeError: 'tuple' object does not support item assignment

# (a,b,c) = (1,2,3)
# print(a,b,c) # 1 2 3

# (a,b,c,d) = (1,2,3) # ValueError: not enough values to unpack (expected 4, got 3)
# a,b,c,d = (1,2,3) # ValueError: not enough values to unpack (expected 4, got 3)
# a,b,c,d,e = (p,q,r,s,t) = t1 # NameError: name 't1' is not defined

# a,b,c,d,e = (p,q,r,s,t)
# print(a,b,c,d,e,p,q,r,s,t) # NameError: name 'p' is not defined

# t = ('a','b','c','d','e')
# t = ('A',)+t[1:]
# print(t) # ('A', 'b', 'c', 'd', 'e')

# t = ('a','b','c','d','e') * (3)
# print(t)

# a = (1,2)
# a1 = ('1','2')
# print(a+a1) # (1, 2, '1', '2')

# a = (1,2,3,4,5,6,7)
# print(a[2:-2])
# print(a[-2:2])
# print(a[:])

# a = ('abcd',('a','b'))
# print(a[1][0] in a[0])

# t = ('a','b','c','d')
# a,b,c,d = t
# 1n,2n,3n,4n = t

# What would be the output of following code if ntpl = ("Hello", "Nita", "How's", "life?")
# ntpl = ("Hello", "Nita", "How's", "life?")
# (a, b, c, d) = ntpl
# print ( "a is:", a)
# print("b is:", b)
# print("c is:", c)
# print("d is:", d)
# ntpl = (a, b, c, d)
# print (ntpl[0][0] + ntpl[1][1], ntpl[1])

# a = 'a','b'
# b = ('a','b')
# print(a == b) # True

# t = ('python') * 3
# print(type(t), t) # str

# t = ('Mega',) * 3
# print(len(t), t) #3

# t = ((1,2),) * 7
# print(t)
# print(len(t[3:8])) # 4

# a = (1,(2,(3,(4,))))
# print(len(a))
# print(a[1][0])
# # print(2 in a)
# z = (2,(1,(2,),1),4)
# print(z[z[0]]) # 4
# print(z[z[z[0]]]) # IndexError: tuple index out of range