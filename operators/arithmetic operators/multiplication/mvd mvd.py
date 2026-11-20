# str * str
print("Hello" * "World")  # TypeError

# list * list
print([10, 20] * [1, 2])  # TypeError

# tuple * tuple
print((10, 20) * (1, 2))  # TypeError

# set * set
print({10, 20} * {1, 2})  # TypeError

# dict * dict
print({1: "A"} * {2: "B"}) # TypeError