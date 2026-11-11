# rfind() is known as the reverse find method in Python. It is used to find the last occurrence of a specified substring in a string. The syntax for the rfind() method is:

# Syntax is: string.rfind(substring, start, end)
#right to left
a="lucky is good boy"

print(a.rfind("y"))#16
print(a.rfind("o"))#15
print(a.rfind("o",11,14))#11
print(a.rfind("lucky"))#0
print(a.rfind("o",14,11))#-1
