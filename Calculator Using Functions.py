# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Function-Based Calculator

"""
LOGIC:
1. Defines independent functions for each operation (add, subtract, multiply, divide, modulus, power).
2. Uses a menu-driven 'while' loop to allow continuous calculations.
3. Performs input validation using try-except to handle non-numeric data.
4. Includes safety checks within the divide and modulus functions to prevent division by zero errors.
5. Calls specific functions based on the user's menu choice and displays the return value.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '7':
        print("Calculator closed.")
        break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    elif choice == '5':
        print("Result:", modulus(a, b))
    elif choice == '6':
        print("Result:", power(a, b))
    else:
        print("Invalid choice! Please select 1-7.")