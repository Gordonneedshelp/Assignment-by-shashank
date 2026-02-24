# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Factorial Program with Steps

"""
LOGIC:
1. Takes an integer as input and checks if it's negative, zero, or positive.
2. For negative inputs, it informs the user that factorial is not defined.
3. For zero, it directly prints that 0! = 1.
4. For positive integers, it uses a 'for' loop to iterate from the number down to 1.
5. In each iteration, it multiplies the current value to a 'factorial' variable and appends the step to a string for display purposes.
"""

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers.")

elif num == 0:
    print("0! = 1")

else:
    factorial = 1
    steps = ""

    for i in range(num, 0, -1):
        factorial *= i
        if i != 1:
            steps += str(i) + " × "
        else:
            steps += "1"

    print(f"{num}! = {steps} = {factorial}")