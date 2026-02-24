# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Simple Calculator with Error Handling

"""
LOGIC:
1. Takes two numeric inputs from the user.
2. Uses a try-except block to handle non-numeric inputs (ValueError).
3. Performs basic arithmetic: Addition (+), Subtraction (-), Multiplication (*).
4. Includes a condition to check for division by zero before performing Division (/) and Modulus (%).
5. Calculates exponentiation using the ** operator.
6. Displays all results in a formatted output.
"""

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handling division safely
    if num2 != 0:
        division = round(num1 / num2, 2)
        modulus = num1 % num2
    else:
        division = "Undefined (Cannot divide by zero)"
        modulus = "Undefined (Cannot divide by zero)"

    # Exponentiation
    power = num1 ** num2

    # Displaying results
    print("\n===== Results =====")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")
    print(f"{num1} % {num2} = {modulus}")
    print(f"{num1} ^ {num2} = {power}")


# Run the calculator
if __name__ == "__main__":
    calculator()