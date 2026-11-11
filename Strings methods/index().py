# index() is a string method in Python that is used to find the first occurrence of a specified substring in a string. The syntax for the index() method is:
# syntax is : string.index(substring/char, start, end)

# left to right

a="tomorrow is sunday"
print(a.index('m'))#2
print(a.index('s', 5, 15))#10
print(a.index('o', 0, 5))#1
print(a.index('r', 0, 5))#3
print(a.index('z'))#ValueError: substring not found
print(a.index('s', 0, 5))#ValueError: substring not found
print(a.index("morr"))#1


