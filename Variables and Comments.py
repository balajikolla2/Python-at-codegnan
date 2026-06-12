Python 3.15.0a6 (tags/v3.15.0a6:15b216f, Feb 11 2026, 12:54:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
b = 20
c = 30
d = a+b+c
print(d)
60

num1 = num2 = num3 = 100
print(num1)
100
print(num2)
100
print(num3)
100
>>> print(num1,num2,num3)
100 100 100
>>> print(id(num1))
140703613374712
>>> print(id(num2))
140703613374712
>>> print(id(num3))
140703613374712
>>> print(id(a))
140703613371832
>>> print(id(b))
140703613372152
>>> print(id(c))
140703613372472
>>> a = 20
>>> b = 40
>>> print(id(a))
140703613372152
>>> print(id(b))
140703613372792
>>> a,b = b,a
>>> print(a)
40
>>> print(id(a))
140703613372792
