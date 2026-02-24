# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Temperature Converter Program

"""
LOGIC:
1. Provides a comprehensive menu for 6 types of temperature conversions (C, F, and K).
2. Uses a 'while' loop to keep the program interactive.
3. Implements standard mathematical conversion formulas inside conditional blocks.
4. Uses try-except to catch invalid numeric inputs.
5. Rounds the final results to two decimal places for better readability.
"""

while True:
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Program exited.")
        break

    try:
        temp = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid input! Enter numeric value.")
        continue

    if choice == '1':
        result = (temp * 9/5) + 32
        print(f"{temp} °C = {result:.2f} °F")

    elif choice == '2':
        result = (temp - 32) * 5/9
        print(f"{temp} °F = {result:.2f} °C")

    elif choice == '3':
        result = temp + 273.15
        print(f"{temp} °C = {result:.2f} K")

    elif choice == '4':
        result = temp - 273.15
        print(f"{temp} K = {result:.2f} °C")

    elif choice == '5':
        result = (temp - 32) * 5/9 + 273.15
        print(f"{temp} °F = {result:.2f} K")

    elif choice == '6':
        result = (temp - 273.15) * 9/5 + 32
        print(f"{temp} K = {result:.2f} °F")

    else:
        print("Invalid choice! Please select 1–7.")

