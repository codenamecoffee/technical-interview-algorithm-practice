"""
7. List Intersection

Return the elements that appear in both lists, without duplicates.

def intersection(a, b):
    pass
"""

a = input("Please, enter list number one (Whatever you wanna write):")
b = input("Please, enter list number one (Whatever you wanna write):")

def intersection(a: list[str], b: list[str]) -> list[str]:
    data_a = {}
    for char in a:
        if char not in data_a:
            data_a[char] = 1

    data_b = {}    
    for char in b:
        if char not in data_b:
            data_b[char] = 1

    print(data_a.keys())
    print(data_b.keys())

    common = set(data_a.keys()) & set(data_b.keys())
    return list(common)

print(intersection(a,b))


# Solution 2
def intersection2(a: list[str], b: list[str]) -> list[str]:
    return list(set(a) & set(b))

print(intersection2(a,b))

"""
Notes:
- The first solution builds dictionaries to store unique elements from each list, then finds the intersection of their keys.
- The second solution is more Pythonic and efficient: it converts both lists to sets and returns their intersection as a list.
- Both solutions ensure that the result contains only unique elements present in both input lists.
- Time complexity for both approaches is O(n + m), where n and m are the lengths of the input lists.
- The order of elements in the result is not guaranteed, since sets are unordered collections.
"""