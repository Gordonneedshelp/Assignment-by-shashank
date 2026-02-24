# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Multiplication Table Program

"""
LOGIC:
1. Inputs the target number and the range end for the table.
2. Uses a 'for' loop to iterate from 1 up to the specified range end.
3. Performs multiplication (num * i) in each iteration.
4. Prints the result in a clean, readable 'num x i = product' format.
"""

num = int(input("Enter number: "))
range_end = int(input("Enter range end: "))

print(f"\nMultiplication Table of {num}")

for i in range(1, range_end + 1):
    print(f"{num} x {i} = {num * i}")