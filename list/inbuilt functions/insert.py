# insert() - Adds an element at a specified position in the list.

# syntax is: list.insert(index, element)


a=[1,2,3,4,5]
a.insert(2,100)
print(a)#[1, 2, 100, 3, 4, 5]

# ex2
a=[1,2,3,4,5]
a.insert(-1,100)
print(a)#[1, 2, 3, 4, 100, 5]

# explaination for last example: In the second example, we are inserting the element 100 at index -1. In Python, negative indices count from the end of the list, so index -1 refers to the last element of the list. Therefore, when we insert 100 at index -1, it is placed just before the last element (5) in the list. The resulting list is [1, 2, 3, 4, 100, 5].
