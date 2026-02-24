# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Movie Ticket Billing System

"""
LOGIC:
1. Takes age, day of the week, and number of tickets as input.
2. Determines the 'base_price' using conditional tiers based on age groups (e.g., <3 is free, 3-12 is child rate).
3. Calculates the initial total by multiplying base price by ticket count.
4. Checks if the day is a weekend (Friday, Saturday, Sunday) to apply a 20% discount.
5. Computes the final amount by subtracting the discount from the total and displays a detailed bill.
"""

try:
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))
except ValueError:
    print("Invalid input! Please enter correct values.")
    exit()

# Base price by age
if age < 3:
    base_price = 0
elif 3 <= age <= 12:
    base_price = 150
elif 13 <= age <= 59:
    base_price = 300
else:
    base_price = 200

# Total amount before discount
total = base_price * tickets

# Weekend discount (20%)
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * total
else:
    discount = 0

final_amount = total - discount

# Display bill
print("\n=== TICKET BILL ===")
print(f"Base Price per Ticket: ₹{base_price}")
print(f"Total before discount: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")