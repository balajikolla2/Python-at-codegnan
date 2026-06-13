#Identity and membership Op

a = [1,2,3,4,5]
b = a
print(a is b)


#compare the values
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)

#compare memory locations

a = [1,2,3]
b = [1,2,3]
print(a is b)

#returns true if variables points to different objects
print(a is not b) 

a = [10,20,30]
print(20 in a)
print(40 not in a)
