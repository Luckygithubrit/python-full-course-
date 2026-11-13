# lstrip() is a string method in Python that returns a copy of the original string with leading whitespace removed. It can also remove specified characters from the beginning of the string.

# syntax is: string.lstrip([chars])

a="   lucky is good boy   "
print(a.lstrip())#lucky is good boy
print(a.lstrip(" "))#lucky is good boy
print(a.lstrip("l"))#ucky is good boy
