# multiple variable is a variable that can hold multiple values or data types. In Python, you can create multiple variables in a single line by separating them with commas. For example:


#ex 1
a, b, c = 1, 2.5, "Hello"
print(a)  # Output: 1
print(b)  # Output: 2.5
print(c)  # Output: Hello

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>

print(a, b, c)

# ex 2

a,b,c=1,2,3,4
print(a,b,c)#ValueError: too many values to unpack (expected 3, got 4)

#when the multiple values are equally stored in variabbles then,the address will be same foe those values

#ex

a,b,c,d=1,2,3,2
print(id(a))#140718353581208
print(id(b))#140718353581232 #same
print(id(c))#140718353581264
print(id(d))#140718353581232 #same

