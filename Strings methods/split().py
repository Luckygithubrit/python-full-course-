# split() is known as a string method in Python that is used to split a string into a list of substrings based on a specified delimiter. By default, the delimiter is whitespace, but you can specify any character or substring as the delimiter.


# syntax is: string.split(delimiter, maxsplit)

a="lucky is good boy"
print(a.split())#['lucky', 'is', 'good', 'boy']

print(a.split("o"))#['lucky is g', '', 'd b', 'y']

print(a.split("o",1))#['lucky is g', 'od boy']

print(a.split(","))#['lucky is good boy']


