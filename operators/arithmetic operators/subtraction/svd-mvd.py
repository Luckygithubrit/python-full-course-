# int - list
print(10 - [1, 2, 3])  # TypeError

# int - tuple
print(10 - (1, 2, 3))   # TypeError

# int - set
print(10 - {1, 2, 3})   # TypeError

# int - dict
print(10 - {1: "a"})    # TypeError

# int - str
print(10 - "hello")     # TypeError