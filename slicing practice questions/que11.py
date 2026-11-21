# A college stores the names of 10 students in a list. Write a program to create a new list containing the last five students followed by the first five students, maintaining their original order within each group.

a=["a","b","c","d","e","f","g","h","i","j"]
b=a[0:5]
c=a[5:]
print("original:",b)#original: ['a', 'b', 'c', 'd', 'e']
print("new list:",c+b)#new list: ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']

