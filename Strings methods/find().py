# find() is a string method in Python that is used to find the first occurrence of a specified substring in a string. The syntax for the find() method is:

# syntax is: string.find(substring/char, start, end)

#left to right

a="lucky is good boy"
print(a.find("y"))#16
print(a.find("o"))#11
print(a.find("lucky"))#0
print(a.find("uCkL"))#-1
print(a.find("d",11,14))#12
