"""
3. Filter and Sort

Given an array of integers, return only the numbers greater than a value k, sorted in ascending order.

def filter_greater(arr, k):
    pass
"""

user_input = input("Please, add a collection  of integer numbers separated by commas (i.e. 1,4,7,-20,...,etc.): ")
string_list = user_input.split(",")

number_list = []
for char in string_list:
    number_list.append(int(char))

user_max = int(input("Please, now enter a k value to use as a min value for the future result: "))

print(f"\nSo, the initial list looks like this: {number_list} and k = {user_max}")

def filter_greater(arr: list[int], k: int) -> list[int]:

    for i in range(0, len(arr) - 1):
        temp_i = i
        for l in range(i, len(arr)):
            if arr[temp_i] > arr[l]:
                temp_value = arr[l]
                arr[l] = arr[temp_i]
                arr[temp_i] = temp_value
                temp_i = l

    print(f"Now the list is sorted in ascending order: {arr}")

    for j in range(len(arr) - 1, -1, -1):
        if arr[j] <= k:
            index = j + 1
            break
        else:
            index = j
      
    if index == len(arr):
        return []
    else:
        print(index)
        return arr[index:]
        
        
print(f"The final result looks like this: {filter_greater(number_list, user_max)}")

# Solución 2 (Pythonic)

def filter_greater(arr: list[int], k: int) -> list[int]:
    return sorted([x for x in arr if x > k])

"""
Notes:
- The current solution manually sorts the list (selection sort) and then finds the first element greater than k.
- This works, but is more verbose and less efficient than using built-in Python features.
- A more Pythonic and efficient solution uses a list comprehension to filter, and the built-in sorted() function to sort:
    sorted([x for x in arr if x > k])
- This approach is O(n log n) due to sorting, and O(n) for filtering.
- Modifying the original list in-place may not always be desired; using sorted() returns a new list.
- The function returns an empty list if no elements are greater than k.
"""