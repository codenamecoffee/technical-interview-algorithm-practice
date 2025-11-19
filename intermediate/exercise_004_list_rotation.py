import random

"""
4. List Rotation

Rotate a list n positions to the right.

Example:
[1, 2, 3, 4, 5], n=2 → [4, 5, 1, 2, 3]

51234 n=1
45123 n=2
34512 n=3

def rotate_right(arr, n):
    pass
"""

arr0 = []
arr1 = [1]
arr2 = [1,2,3,4,5,6,7,8,9]

n1 = -1
n2 = random.choice([0, 9]) 
n3 = random.randint(1, 8) 

def rotate_right(arr: list[int], n: int) -> list[int]:
    print()
    if arr:
        if n <= 0:
            print("n is less or equal to 0.")
            return arr
        else:
            result = arr[:]
            for i in range(0,n):
                result.insert(0, result.pop())
            return result
    else:
        print("The list is empty.")
        return []

print(f"\narr0 = {arr0} rotated n1 = {n1}: {rotate_right(arr0, n1)}")
print(f"\narr0 = {arr0} rotated n2 = {n2}: {rotate_right(arr0, n2)}")
print(f"\narr0 = {arr0} rotated n3 = {n3}: {rotate_right(arr0, n3)}")
print(f"\narr1 = {arr1} rotated n1 = {n1}: {rotate_right(arr1, n1)}")
print(f"\narr1 = {arr1} rotated n2 = {n2}: {rotate_right(arr1, n2)}")
print(f"\narr1 = {arr1} rotated n3 = {n3}: {rotate_right(arr1, n3)}")
print(f"\narr2 = {arr2} rotated n1 = {n1}: {rotate_right(arr2, n1)}")
print(f"\narr2 = {arr2} rotated n2 = {n2}: {rotate_right(arr2, n2)}")
print(f"\narr2 = {arr2} rotated n3 = {n3}: {rotate_right(arr2, n3)}")

# Solution 2 (Pythonic)

def rotate_right(arr: list[int], n: int) -> list[int]:
    if not arr:
        print("The list is empty.")
        return []
    n = n % len(arr) if n > 0 else 0
    if n == 0:
        print("No rotation performed.")
        return arr[:]
    return arr[-n:] + arr[:-n]

"""
Notes:
- This implementation rotates the list to the right by repeatedly popping the last element and inserting it at the front.
- It creates a copy of the original list, so the input is not modified.
- Handles empty lists and non-positive n values gracefully.
- Time complexity is O(n * k), where n is the list length and k is the number of rotations.
- For large lists or many rotations, using slicing (arr[-n:] + arr[:-n]) is more efficient (O(n)).

# Solution 2: 
- Rotates a list n positions to the right using slicing.
- Handles empty lists and non-positive n values gracefully.
- Uses n % len(arr) to support n greater than the list length.
- Does not modify the original list.
- Time complexity is O(n), where n is the length of the list.
- For large lists or many rotations, this is more efficient than repeated pop/insert.

Curiosity: "Ternary operator"

n = n % len(arr) if n > 0 else 0

"""



