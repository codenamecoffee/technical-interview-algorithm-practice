"""
5. First Non-Repeated Character

Given a string, return the first character that does not repeat.
If all characters repeat, return None.

def first_unique_char(s):
    pass
"""

string = input("Please, enter a string (to determine its first repeated character): ")

def first_unique_char(s: str) -> str:
    result = ""
    if s:
        data = {}
        for char in s:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1

        for key, value in data.items():
            if value == 1: 
                result = key
                break
    
    return result

results = first_unique_char(string)
print(f"The first non-repeated character in the string: {string} is: {results if results else None }")