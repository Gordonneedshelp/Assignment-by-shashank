# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Simple ATM Machine Program

"""
LOGIC:
1. Initializes a starting balance (e.g., ₹10000).
2. Uses a 'while True' loop to keep the system running until the user chooses to exit.
3. Provides a menu for Checking Balance, Depositing money, and Withdrawing money.
4. For Deposits: Adds the input amount to the current balance if it's positive.
5. For Withdrawals: Deducts the amount if it's positive and ensures a minimum balance (₹500) is maintained.
6. Uses try-except blocks to prevent crashes from invalid numeric inputs.
"""

balance = 10000  # Initial balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        print(f"Current Balance: ₹{balance}")

    elif choice == '2':
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print(f"New Balance: ₹{balance}")
            else:
                print("Invalid amount.")
        except ValueError:
            print("Invalid input.")

    elif choice == '3':
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount > 0 and balance - amount >= 500:
                balance -= amount
                print("Withdrawal successful!")
                print(f"New Balance: ₹{balance}")
            else:
                print("Insufficient balance or minimum ₹500 must remain.")
        except ValueError:
            print("Invalid input.")

    elif choice == '4':
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice! Please select 1-4.")