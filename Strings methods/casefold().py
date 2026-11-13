# casefold() is a string method in Python that returns a case-insensitive version of the original string. It is similar to the lower() method, but it is more aggressive in its case conversion, making it suitable for case-insensitive comparisons.

# syntax is: string.casefold()

a="LUCKY IS GOOD BOY"
print(a.casefold())#lucky is good boy

print(a.casefold().isupper())#False

# ex2
b="HELLO WORLD"
print(b.casefold())#hello world
print(b.casefold().isupper())#False
