# strip() is a string method in Python that returns a copy of the original string with leading and trailing whitespace removed. It can also remove specified characters from the beginning and end of the string.

# syntaxx is: string.strip([chars])

a="   lucky is good boy   "
print(a.strip())#lucky is good boy


#ex2
a="lucky is good boy"
print(a.strip("l"))#ucky is good boy
print(a.strip("y"))#lucky is good boy