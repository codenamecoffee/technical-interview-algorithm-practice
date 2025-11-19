"""
Caesar Cipher (strings + lógica)

Implement a simple Caesar cipher that shifts letters by k positions.
Ignore spaces and punctuation.

Example: shift=3
"attack" → "dwwdfn"

"""

string = input("Please, enter a word: ")
number = int(input("Please, now enter how many moves you want to apply on it: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"

def word_shift(word: str, shift: int) -> str:
    result = ""
    for char in word.lower():
        if char in alphabet:
            new_char_index = (alphabet.index(char) + shift) % 26 # Useful to keep in range on the alphabet
            result += alphabet[new_char_index]
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

print(f"\nThe result: {word_shift(string, number)}")

"""
Notes:
- The function now correctly handles wrap-around using modulo 26.
- Non-alphabetic characters (spaces, punctuation) are preserved.
- The input is converted to lowercase to handle both cases uniformly.
- Make sure the alphabet string is in the correct order and includes all 26 letters.
- Time complexity is O(n), where n is the length of the input string.
"""