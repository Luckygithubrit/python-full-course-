# A company stores its revenue for all 12 months. Write a program to extract the revenue generated during the second quarter and fourth quarter separately.

revenue = [10000, 3300, 15000, 28000, 28000, 22000, 25000, 21000, 30000, 82000, 45000, 40000]
second=revenue[3:6]
fourth=revenue[9:]
print("second quarter",second)#second quarter [28000, 28000, 22000]
print("fourth quarter",fourth)#fourth quarter [82000, 45000, 40000]