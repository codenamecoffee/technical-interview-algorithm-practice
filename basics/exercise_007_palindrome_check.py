"""
Check if a word reads the same backward.
Input: "radar" → Output: True
"""

word = str(input("Please, enter a word (To check if is palindrome or not): "))

if word == word[::-1]:
    print("The entered word is a palindrome.")
else:
    print("The entered word is not a palindrome.")


"""
Notes:
- Palindromes can have even or odd length.
- word[::-1] creates a reversed version of the string.
- This solution works for any string, regardless of its length.
"""

"""
More curiosities (Practicing slicing):

"""
word2 = str(input("\nPlease, add a word for slice practicing: "))
mid = len(word2) // 2        # => '//' integer division
print(f"word length: {len(word2)}")
print(f"mid: {mid}")
first_half = word2[:mid]
second_half = word2[mid+1:]
first_half_inverted = word2[mid+1::-1]  # If not specifying the finish position, then IT GETS included.
second_half_inverted = word2[:mid:-1]  # It goes from last position to mid position, without including it.
print(first_half)     
print(second_half)  
print(first_half_inverted)
print(second_half_inverted)

"""
Efficiency notes:
- The palindrome check (word == word[::-1]) has O(n) time complexity, where n is the length of the string.
    - word[::-1] creates a reversed copy of the string, which is O(n).
    - The equality comparison also takes O(n) time in the worst case.
    - Total time complexity: O(n).
- Slicing operations (like word2[:mid], word2[mid+1:], word2[mid+1::-1], word2[:mid:-1]) are also O(k), where k is the length of the resulting slice.
- All these operations are efficient for small to moderately sized strings, but for very large strings, the time and memory used are proportional to the string length.
"""
