# rindex is known as the reverse index method in Python. It is used to find the last occurrence of a specified substring in a string. The syntax for the rindex() method is:

# syntax is: string.rindex(substring, start, end)
#right to left


a="lucky is good boy"
print(a.rindex("y"))#16
print(a.rindex("o"))#15
# print(a.rindex("o",14,11))#ValueError: substring not found
print(a.rindex("lucky"))#0
print(a.rindex("o",11,14))#11

