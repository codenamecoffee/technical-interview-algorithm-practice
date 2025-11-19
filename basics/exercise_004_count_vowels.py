"""
Count how many vowels appear in a string.
Input: "programming" → Output: 3
"""

string = "Practicing algorithms with Python, leveling up."
vowels = {"a","e","i","o","u"}
count = 0

for char in string:
    if char.lower() in vowels: # Case-insensitive check
        count += 1

print(f"La cantidad de vocales en la frase: \"{string}\" es: {count}")

"""
Notes:
- Using a set for vowels makes the membership test faster.
- char.lower() ensures the count is case-insensitive.
- The algorithm is O(n), where n is the length of the string.

Why not a list for the vowels?

vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_set = {'a', 'e', 'i', 'o', 'u'}
char = 'e'

# List: checks each element one by one (up to 5 checks)
char in vowels_list  # O(n)

# Set: uses hash, finds almost instantly
char in vowels_set   # O(1)


"""