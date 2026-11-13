# extend() is a built-in method in Python that is used to add multiple elements to the end of a list. It takes an iterable (like a list, tuple, or set) as an argument and appends each element of that iterable to the end of the list.

# syntax is: list.extend(iterable)


a=[1,2,3,4,5]
a.extend([6,7,8])
print(a)#[1, 2, 3, 4, 5, 6, 7, 8]

# ex2
a=[1,2,3,4,5]
a.extend((6,7,8))
print(a)#[1, 2, 3, 4, 5, 6, 7, 8]

# ex3

a=[1,2,3,4,5]
a.extend({'a':1,'b':2})
print(a)#[1, 2, 3, 4, 5, 'a', 'b']  