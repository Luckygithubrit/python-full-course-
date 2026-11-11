# count is just a string method in Python that is used to count the number of occurrences of a specified substring in a string. The syntax for the count() method is:

# syntax is: string.count(substring/char, start, end)


a="Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked"
print(a.count("Peter"))#2
print(a.count("peck"))#2
print(a.count("peppers"))#2
print(a.count("p", 0, 10))#1
print(a.count("P", 0, 10))#2
print(a.count("p"))#14
