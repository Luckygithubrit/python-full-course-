# replace is a string method in Python that is used to replace occurrences of a specified substring with another substring. The syntax for the replace() method is:

# syntax is: string.replace(old, new, count)
a="licky is good boy"
print(a.replace("licky","food",1))#food is good boy
print(a.replace("good","bad",1))#licky is bad boy
print(a.replace("boy","girl",1))#licky is good girl
print(a.replace("licky","food"))#food is good boy



# ex 2


a="Peter Piper picked a peck of pickled peppers.A peck of pickled peppers Peter Piper picked."
print(a.replace("Peter","lucky",1))#lucky Piper picked a peck of pickled peppers.A peck of pickled peppers peter Piper picked.
print(a.replace("Peter","lucky",2))#lucky Piper picked a peck of pickled peppers.A peck of pickled peppers lucky Piper picked.



