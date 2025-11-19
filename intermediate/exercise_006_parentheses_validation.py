"""
6. Parentheses Validation 
Check if a string containing ()[]{} has correct (balanced) parentheses.

def is_valid_parentheses(s):
    pass
"""

# Test case NOT passing: (Now corrected)
# ")))(((" is balanced according to my solution, which is wrong.

string = input("\nPlease, enter a string with all types of parentheses (to determine if it's balanced): ")

def is_valid_parentheses(s: str) -> bool:
    result = True
    right = []
    left = []
    right_parentheses = {"(","[","{"}
    left_parentheses = {")","]","}"}
    for char in s:
        if char in right_parentheses:
            right.append(char)
        if char in left_parentheses and len(right) >= len(left): # Correction added.
            left.insert(0, char)

    if (len(right) == len(left)):
        for i in range(0, len(right)):
            match right[i]:
                case "(":
                    if left[i] != ")":
                        result = False
                        break
                case "[":
                    if left[i] != "]":
                        result = False
                        break
                case "{":
                    if left[i] != "}":
                        result = False
                        break
    else:
        result = False

    return result

results = is_valid_parentheses(string)
print("\nThe entered string is balanced.") if results else print("\nThe entered string is not balanced.")

"""
Notes on this approach:
- This solution collects all opening parentheses in one list (right) and all closing parentheses in another (left, inserted at the front).
- It then compares the lists by position, assuming that the order of opening and closing matches when reversed.
- This works for many simple cases, but does not guarantee correct nesting for all possible inputs.
- It does not use a true stack structure, so it may fail for complex or deeply nested cases.
- Time complexity is O(n), but correctness is not guaranteed for all valid/invalid parenthesis patterns.
"""

# Solution 2
def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in "([{":
            stack.append(char)  # Push opening bracket onto the stack
        elif char in ")]}":
            # If stack is empty or top of stack doesn't match, it's invalid
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()  # Pop the matching opening bracket
    return not stack  # If stack is empty, all brackets matched


"""
Notes on the stack approach:
- Uses a stack to track opening parentheses.
- For each closing parenthesis, checks if it matches the most recent opening one.
- Ensures both correct count and correct nesting/order.
- Time complexity is O(n), where n is the length of the string.
- This is the standard and most reliable way to validate balanced parentheses in coding interviews and real-world code.
"""