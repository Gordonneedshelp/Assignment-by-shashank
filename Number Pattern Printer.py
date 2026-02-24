# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Pattern Printing Program

"""
LOGIC:
1. Takes the height (rows) of the patterns from the user.
2. Implements four distinct patterns using nested 'for' loops:
   - Pattern 1: Prints increasing numbers (1, 1 2, 1 2 3) by using the inner loop variable.
   - Pattern 2: Prints the current row number repeated (1, 2 2, 3 3 3) using string multiplication.
   - Pattern 3: Prints numbers in reverse order per row and decreasing rows.
   - Pattern 4: Prints a pyramidal sequence (1, 121, 12321) by using two inner loops for ascending and descending parts.
"""

rows = int(input("Enter height: "))

# Pattern 1
print("\nPattern 1")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 2
print("\nPattern 2")
for i in range(1, rows + 1):
    print((str(i) + " ") * i)

# Pattern 3
print("\nPattern 3")
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Pattern 4
print("\nPattern 4")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()