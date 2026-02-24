# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Taking sentence input

"""
LOGIC:
1. Inputs a full sentence and immediately performs character count analysis (total length and length minus spaces).
2. Uses the '.split()' method to break the sentence into a list of words and calculate the word count.
3. Applies built-in string methods '.upper()', '.lower()', and '.title()' for formatted case conversions.
4. Accesses the first element ([0]) and last element ([-1]) of the word list.
5. Reverses the entire sentence using slicing '[::-1]' and displays all aggregated results.
"""
sentence = input("Enter a sentence: ")

# Original sentence
print("\nOriginal:", sentence)

# Characters count
char_with_spaces = len(sentence)
char_without_spaces = len(sentence.replace(" ", ""))

# Word count
words = sentence.split()
word_count = len(words)

# Case conversions
uppercase = sentence.upper()
lowercase = sentence.lower()
titlecase = sentence.title()

# First & Last word
if word_count > 0:
    first_word = words[0]
    last_word = words[-1]
else:
    first_word = ""
    last_word = ""

# Reversed sentence
reversed_sentence = sentence[::-1]

# Display results
print("Characters (with spaces):", char_with_spaces)
print("Characters (without spaces):", char_without_spaces)
print("Words:", word_count)
print("UPPERCASE:", uppercase)
print("lowercase:", lowercase)
print("Title Case:", titlecase)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)