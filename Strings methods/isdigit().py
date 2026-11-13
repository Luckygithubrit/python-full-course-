# isdigit() is a string method in Python that returns True if all the characters in the string are digits (0-9) and there is at least one character, otherwise it returns False. If the string is empty or contains any non-digit characters, it will return False.

# syntax is: string.isdigit()

a="123456"
print(a.isdigit())#True

b="123456abc"
print(b.isdigit())#False

c="123 456"
print(c.isdigit())#False

d="123.456"
print(d.isdigit())#False