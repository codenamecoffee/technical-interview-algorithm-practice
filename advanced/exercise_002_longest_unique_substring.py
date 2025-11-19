"""
Longest Unique Substring Length

Concepts: sliding window, sets/dicts, two pointers

Given a string, return the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
(substring = "abc")

Input: "bbbbb"
Output: 1

This is a classic interview problem.
It requires using the sliding window technique.
"""

string = input("Please, enter a phrase (to determine its longest substring without repeating characters): ")

def longest_unique_substring(string: str) -> int:
    left_pointer = 0
    unique_chars = set()
    longest = 0

    for right_pointer in range(0, len(string)):
        char = string[right_pointer] 
        if(char in unique_chars):
            deleted_char = string[left_pointer]
            unique_chars.remove(deleted_char)
            left_pointer += 1
            while(deleted_char != char):
                deleted_char = string[left_pointer]
                unique_chars.remove(deleted_char)
                left_pointer += 1

        unique_chars.add(char)
        # longest = max(longest, len(unique_chars))
        longest = max(longest, right_pointer - leftpointer + 1)

    return longest

print(f"The longest unique substring according to the phrase you entered, it's {longest_unique_substring(string)} characters long.")

"""
Notes:
- The function uses the sliding window technique with two pointers and a set to track unique characters.
- When a repeated character is found, the left pointer advances and removes characters from the set until the duplicate is gone.
- The maximum length is updated at each step.
- To correctly calculate the window size, use (right_pointer - left_pointer + 1): the +1 is crucial because both pointers are inclusive, ensuring the count reflects the actual number of characters in the current window.
- Time complexity is O(n), where n is the length of the input string.
"""