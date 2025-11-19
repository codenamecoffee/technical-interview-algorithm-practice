"""
Given a string, return it reversed.
Input: "hello" → Output: "olleh"
"""

normal_str = "Practicing algorithms with python."
reversed_str1 = ""

# Solution 1: Manual reversal using a for loop
# Iterate from the last character to the first (using a negative step in range)
for i in range(len(normal_str) - 1, -1, -1): 
    reversed_str1 += normal_str[i]

print(reversed_str1)

# Note:
# - Strings in Python are immutable, so you cannot modify them in place.
# - Each concatenation creates a new string, which is less efficient for very long strings.

# Solution 2: Using slicing (more Pythonic and efficient)
reversed_str2 = normal_str[::-1]
print(reversed_str2)

"""
Efficiency:
- Both solutions have O(n) time complexity, where n is the length of the string.
- The slicing method is more concise and generally faster in Python.

Notes:
- Strings are immutable in Python, so all reversal methods create a new string.
- For very large strings, using ''.join(reversed(normal_str)) is also efficient.
"""