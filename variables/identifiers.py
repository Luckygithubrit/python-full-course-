# identifier is a name used to identify a variable, function, class, module, or other object in Python. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores, and digits (0 to 9). Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case-sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python.


rule 1:
  # identifier cannot be akeyword
if="hi"
print(if)#SyntaxError: invalid syntax

rule 2:
  
# identifier cannot start with a digit
  
  1a=10
  print(1a)#SyntaxError: invalid syntax

rule 3:
  # identifier can start with an underscore
_a=10
print(_a)#10

rule 4:
  # identifier can start with a letter
a=10
print(a)#10

rule 5:
  # identifier can contain digits
a1=10
print(a1)#10

rule 6:
  # identifier cannot contain non alphanumeric characters
a@=10
print(a@)#SyntaxError: invalid syntax
  