"""
Subarray With Target Sum (positive integers)

Concepts: sliding window, partial sums

Statement

Given an array of positive integers and a target value, find the minimal length of a contiguous subarray 
whose sum is ≥ target.

If no such subarray exists, return 0.

Input:

arr = [2, 3, 1, 2, 4, 3], target = 7

Output:

2

Because [4, 3] is the shortest subarray with sum ≥ 7.

This is a problem that can appear on HackerRank with a twist.
"""

user_input = input("(1) - Please, enter a list of integer numbers separated with commas (i.e. 1,3,-33,9,0,..., etc.): ")
user_input = user_input.replace(" ", "")
nums = [int(x) for x in user_input.split(",")]

print(f"\n=> The number list that will be used: {nums}")
user_input = int(input("\n(2) - Now, please enter a **target value** to determine the minimal length of a \n" 
+ "contiguous subarray of the number list (previously entered), whose sum is >= target value: "))

def minimal_subarray_length(nums: list[int], target: int) -> int:
    left_pointer = 0
    right_pointer = 0
    min_length = 0
    current_sum = 0

    while(right_pointer < len(nums) and nums[right_pointer] != target):
        if current_sum < target:
            print(f"Siguiente numero para sumar: {nums[right_pointer]}")
            current_sum += nums[right_pointer]
            print(f"Suma actual: {current_sum}")
            right_pointer += 1
        else: 
            if min_length == 0:
                min_length = right_pointer - left_pointer
            else:
                min_length = min(min_length, right_pointer - left_pointer)

            print(f"min_lentgh: {min_length}")
            print(f"Tenemos que achicar la current sum:")
            
            while not current_sum < target:
                print(f"Restamos: {nums[left_pointer]}")
                current_sum -= nums[left_pointer]
                print(f"Suma actual: {current_sum}")
                left_pointer += 1

    if right_pointer < len(nums):
        return 1
    else:
        right_pointer -= 1
        while left_pointer < right_pointer and current_sum >= target:
                print(f"Restamos: {nums[left_pointer]}")
                current_sum -= nums[left_pointer]
                print(f"Suma actual: {current_sum}")
                left_pointer += 1
                if current_sum >= target:
                    min_length = right_pointer - left_pointer
                    print(f"Actualizamos min_length: {min_length}")
                
        return min_length
        
print(f"The minimal subarray length greater or equal to {user_input} is: {minimal_subarray_length(nums, user_input)}.")



# Solucion 2 (Pytonic)

def minimal_subarray_length(nums: list[int], target: int) -> int:
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

"""
Notes:
- The function uses the sliding window technique to find the minimal length of a contiguous subarray with sum ≥ target.
- Two pointers (left and right) define the window, and current_sum tracks the sum within the window.
- When current_sum ≥ target, the window is shrunk from the left to find the shortest valid subarray.
- min_length is initialized to infinity and updated whenever a valid window is found.
- If no such subarray exists, the function returns 0.
- Time complexity is O(n), where n is the length of the input list.
- This is the standard and most efficient approach for this problem.
"""