# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Number Statistics Program

"""
LOGIC:
1. Inputs the count of numbers to be processed and validates it as a positive integer.
2. Uses a 'for' loop to collect the specified amount of numbers.
3. Implements a nested 'while' loop with try-except to handle errors for each individual number entry.
4. Stores all valid numbers in a Python list.
5. Aggregates data using sum(), max(), and min() functions.
6. Calculates the arithmetic mean (average) and prints a statistical summary.
"""

try:
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Please enter a number greater than 0.")
        exit()
except ValueError:
    print("Invalid input! Please enter an integer value.")
    exit()

numbers = []

for i in range(count):
    while True:
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

total = sum(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

print("\n=== RESULTS ===")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)