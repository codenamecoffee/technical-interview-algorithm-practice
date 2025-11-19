"""
Balance Parentheses With Extra Characters

Concepts: stacks, validation, strings, algorithms

Statement

Given a string containing:
- letters
- spaces
- parentheses: ( and )

You must remove the minimum number of parentheses to make the string valid.

Input:

"a)b(c)d"

Output:

"ab(c)d"

Input:

"lee(t(c)o)de)"

Output:

"lee(t(c)o)de"

This problem appears on LeetCode Medium/Hard.
It requires a smart logic with stacks or a double pass approach.

#Note:  

- This is similar to a previous exercise about checking if a string is balanced with parentheses, but here you must actually 
remove the minimum number of invalid parentheses to make the string valid. Order and matching are crucial for a correct solution.

"""

string = input("Please, enter a phrase with only letters, spaces and curvy brackets (balanced or not): ")
string = string.replace(".", "")

def balance_curvy_brackets(string: str) -> str: 
    result = string[:]
    closing_indexes = []
    opening_indexes = []
    for position, char in enumerate(string): 
        match char:
            case "(":
                opening_indexes.append(position)
            case ")":
                if len(opening_indexes) == 0:
                    closing_indexes.append(position)
                else:
                    _= opening_indexes.pop()

    for i in opening_indexes:
        result = result[:i] + result[i+1:]

    for j in closing_indexes:
        result = result[:j] + result[j+1:]
    
    return result

print(f"Balanced phrase: {balance_curvy_brackets(string)}")

"""
Notes:
- The function removes the minimum number of parentheses to make the string valid.
- It uses two lists to track the indices of unmatched opening and closing parentheses.
- The string is traversed with enumerate(), which provides both the index and the character at each step.
- When an opening parenthesis is found, its index is stored; when a closing parenthesis is found, it is matched with the last opening if possible, otherwise its index is stored as unmatched.
- At the end, all unmatched parentheses (indices in opening_indexes and closing_indexes) are removed from the string.
- Important: initializing two lists on the same line (e.g., a = b = []) makes them refer to the same list object, which can cause bugs. Always initialize them separately.
- enumerate() yields (index, value) pairs, so you can access both the position and the character directly in the loop.
- string.index(char) always returns the first occurrence of char in the string, not necessarily the current position in a loop. This can lead to incorrect removals if there are repeated characters.
- Removing characters by index should be done in reverse order or by building a new string, to avoid shifting indices.
- This approach ensures only the minimum number of parentheses are removed, preserving the order and content of the valid string.
"""