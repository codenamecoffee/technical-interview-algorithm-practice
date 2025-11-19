"""
8. Maximum Subarray Sum (Simplified Kadane)

Return the maximum sum of a contiguous subarray in an array.

Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6

def max_subarray(nums):
    pass
"""
                                            
number_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]   
                                                
def max_subarray(nums: list[int]) -> int:
    if not nums:
        print("The list is empty")
        return 0
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i]) # Equals to nums[i] only when current_sum is negative. 
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray(number_list))

"""
Notes:
- This implementation uses Kadane's algorithm to find the maximum sum of a contiguous subarray in O(n) time.
- At each step, it decides whether to extend the current subarray or start a new one from the current element.
- Handles negative numbers correctly: if all numbers are negative, it returns the largest (least negative) number.
- Time complexity is O(n), where n is the length of the input list.
- This is the standard and most efficient approach for this problem in interviews and real-world scenarios.
"""