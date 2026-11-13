# isnumeric() is a string method in Python that returns True if all the characters in the string are numeric characters, and False otherwise. If the string is empty or contains any non-numeric characters, it will return False.

# syntax is: string.isnumeric()

a="123456"
print(a.isnumeric())#True

b="123456abc"
print(b.isnumeric())#False

c=""
print(c.isnumeric())#False

d="123 456"
print(d.isnumeric())#False

e="123.456"
print(e.isnumeric())#False

f="2/4"
print(f.isnumeric())#False

