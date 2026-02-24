# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Palindrome Checker

"""
LOGIC:
1. Inputs a string (word or number) from the user.
2. Normalizes the input to lowercase to ensure case-insensitive comparison.
3. Utilizes Python's advanced slicing technique '[::-1]' to create a reversed copy of the string.
4. Compares the original 'clean' text with the 'reversed' text.
5. If they are identical, the input is declared a PALINDROME; otherwise, it is NOT.
"""

text = input("Enter word or number: ")

clean_text = text.lower()
reversed_text = clean_text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

if clean_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")