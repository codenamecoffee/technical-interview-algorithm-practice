"""
1. Pairwise Sums

Given an array of integers, return a new array where each element is the sum of each consecutive pair.
Example: [3, 8, 2, 7] → [11, 10, 9].

Complete the function:

def pair_sums(arr):
    pass

"""
try:
    user_input = input("Please, enter integer numbers separated by commas (i.e. : 1,3,22,10,..., etc ): ")
    if not user_input: # User pressed Enter directly without entering any numbers.
        arr = []
    else: 
        arr = [int(x) for x in user_input.split(",")]

except ValueError:
    print("Invalid input. An empty list will be used instead.")
    arr = []

def pair_sums(arr: list[int]) -> list[int]:
    
    cardinal = len(arr)
    if cardinal == 0:
        print("The list is empty.")
        return []
    elif cardinal == 1:
        print("The list has only one element.")
        return [arr[0]]
    else:
        result = []
        for i in range(1, cardinal):
            result.append(arr[i-1] + arr[i])
        return result

print(f"Result: {pair_sums(arr)}")

# Solution 2
def pair_sums(arr: list[int]) -> list[int]:
    return [arr[i] + arr[i+1] for i in range(len(arr)-1)]


"""
Notes:
- The function handles empty input, single-element lists, and invalid input gracefully.
- Time complexity is O(n), where n is the length of the input list.
- The main loop sums each pair of consecutive elements.
- A more Pythonic solution uses a list comprehension: [arr[i] + arr[i+1] for i in range(len(arr)-1)]
- Returning an empty list for empty or single-element input is also valid, as there are no pairs to sum.

Why the Pythonic solution does not go out of range:
- The list comprehension [arr[i] + arr[i+1] for i in range(len(arr)-1)] iterates i from 0 up to len(arr)-2.
- This ensures that arr[i+1] is always a valid index (the last value for i is len(arr)-2, so i+1 is len(arr)-1).
- If the input list has 0 or 1 element, range(len(arr)-1) produces an empty range, so the loop does not execute and an empty list is returned.
- This approach is safe and avoids IndexError by design.

"""