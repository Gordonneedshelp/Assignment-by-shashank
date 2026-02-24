# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Leap Year Checker

"""
LOGIC:
1. Takes a year as input and handles invalid data using try-except.
2. Implements the standard leap year algorithm logic:
   - A year is a leap year if (it is divisible by 4) AND (not divisible by 100 OR divisible by 400).
3. Provides a detailed explanation (reasoning) for whether the year is a leap year or not based on these conditions.
"""

try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input! Enter a valid year.")
    exit()

# Leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a LEAP YEAR.")
    print("Reason: Divisible by 4 and not divisible by 100 unless divisible by 400.")
else:
    print(f"{year} is NOT a leap year.")
    print("Reason: Does not satisfy leap year conditions.")