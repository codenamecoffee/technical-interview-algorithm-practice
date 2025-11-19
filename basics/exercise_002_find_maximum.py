"""
Return the largest element in a given list.
Input: [1, 9, 2, 7] → Output: 9
"""

data = [1, 9, 2, 7]

# Solution 1: Manual search using slicing
if data: # Using truthy and falsy values
    max_value = data[0] # Initialize with the first element

    for i in data[1:]: # Starting from second item in data, if exists. Otherwise, the for does not execute. 
        if i > max_value: 
            max_value = i

print(f"My number list is: {data}")
print(f"The biggest value is: {max_value}")

    # However, data[1: ] creates a copy of the list, which is less efficient for very large lists.
    # Here, a cleaner way: using range(initial position, last position - 1)

if data:
    max_value2 = data[0] 
    for i in range(1, len(data)): # From second item to the last, if they exist. Otherwise, it does not execute.
        if data[i] > max_value2:
            max_value2 = data[i]

print(f"The biggest value_V2 is: {max_value2}")


# Solution 3: Using max():

if data: 
    max_value3 = max(data)

print(f"The biggest value_V3 is: {max_value3}")


"""
Efficiency:
- All three solutions have O(n) time complexity, where n is the number of elements in the list.
- Each element is checked once, and each comparison is O(1).
- The slicing approach (data[1:]) creates a new list, which adds a small overhead for large lists.
- The built-in max() function is also O(n) and is the recommended approach in real-world Python code.

Notes:
- Always check if the list is not empty before accessing elements to avoid IndexError.
- Using built-in names like 'max' as variable names is not recommended.
"""
