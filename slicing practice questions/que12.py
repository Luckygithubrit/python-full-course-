# A programming application stores the following numbers:
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Using slicing:
# 1. Extract the first five elements.
a=numbers[0:5]
print(a)#[10, 20, 30, 40, 50]
# 2. Reverse the extracted list.
reverse=a[-1::-1]
print(reverse)#[50, 40, 30, 20, 10]
# 3. Combine the original extracted list and its reversed version to create a palindrome list.
print(a+reverse)#[10, 20, 30, 40, 50, 50, 40, 30, 20, 10]
# Expected output:
# [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]

