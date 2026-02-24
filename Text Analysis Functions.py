# Name: Param Jaiswal
# Branch: CSE Data Science Branch
# Advanced Text Analyzer

"""
LOGIC:
1. Converts the entire text to lowercase and splits it into a list of words.
2. Uses generator expressions to count vowels and consonants by iterating through the string characters.
3. Calculates word frequency using a dictionary to map each word to its occurrence count.
4. Determines the longest word using the 'max' function with 'key=len'.
5. Performs additional string manipulations like reversing and removing vowels to provide in-depth analysis.
"""

def analyze_text(text):
    words = text.lower().split()
    vowels = "aeiou"

    word_count = len(words)
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    consonant_count = sum(1 for char in text.lower() if char.isalpha() and char not in vowels)
    reversed_text = text[::-1]
    palindrome = text.lower() == reversed_text.lower()
    no_vowels = "".join([c for c in text if c.lower() not in vowels])

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    longest = max(words, key=len) if words else ""

    print("\n=== TEXT ANALYSIS ===")
    print("Words:", word_count)
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Reversed:", reversed_text)
    print("Palindrome:", "Yes" if palindrome else "No")
    print("Without vowels:", no_vowels)
    print("Longest word:", longest)
    print("Word Frequency:", freq)


# Taking input
text = input("Enter text: ")
analyze_text(text)