# A company generates employee IDs in the format "EMP20261125". Write a program to extract the employee's joining year and employee number separately.

a="EMP20261125"
joiningyear=a[3:7]
empno=a[7:]
print("joining year:",joiningyear)#joining year: 2026
print("empno:",empno)#empno: 1125