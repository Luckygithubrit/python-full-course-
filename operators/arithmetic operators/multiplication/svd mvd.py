# int * str
print(3 * "Python")  # PythonPythonPython

# int * list
print(2 * [10, 20])  # [10, 20, 10, 20]

# int * tuple
print(2 * (10, 20))  # (10, 20, 10, 20)

# int * set
print(2 * {10, 20})  # TypeError

# int * dict
print(2 * {1: "A"})  # TypeError