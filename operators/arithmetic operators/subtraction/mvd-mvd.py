# str - str is not supported.
# list - list is not supported.
# tuple - tuple is not supported.
# set - set supports subtraction as a set difference operation.


# str - str (Not Supported)
print("Hello" - "World")  # TypeError

# list - list (Not Supported)
print([10, 20, 30] - [10, 20])  # TypeError

# tuple - tuple (Not Supported)
print((10, 20, 30) - (10, 20))  # TypeError

# set - set
print({10, 20, 30} - {10, 20})  # {30}