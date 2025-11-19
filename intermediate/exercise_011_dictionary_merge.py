"""
Dictionary Merge

Given two dictionaries, create a new dictionary where:

- Keys present in both dictionaries have their values added.
- Keys that appear in only one dictionary keep their original value.

Example:

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 5}
→ {"x": 1, "y": 5, "z": 5}
"""

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 5}


def join_all(dict_a: dict[str, int], dict_b: dict[str, int]) -> dict[str, int]:
    result = dict(dict_a)  
    for key, value in dict_b.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

print(join_all(a,b))

"""
Notes:
- The current solution is correct and efficient, but the order of keys in the result is not guaranteed because sets are unordered.
- If you want to preserve the order (first keys from dict_a, then new keys from dict_b), start with a copy of dict_a and update/add values from dict_b.
- In Python 3.7+, dictionaries preserve insertion order.
- Time complexity is O(n + m), where n and m are the number of keys in each dictionary.
"""