
'''
### MiniMaxSum

Description:
This exercise consists of finding the minimum and maximum sums that can be obtained by 
summing exactly four out of five given positive integers. The goal is to print both values 
on a single line, separated by a space.

This type of problem is common on programming platforms like HackerRank, where the focus is 
on practicing list manipulation and partial sum calculations. The challenge lies in avoiding 
integer overflow and correctly selecting the four smallest and four largest values.

Solution:
The strategy used here is to copy the original list and, in four iterations, remove the smallest 
and largest elements respectively to calculate the minimum and maximum sums. This ensures that the 
four smallest values are summed for the minimum sum, and the four largest for the maximum sum.

The function does not return any value, but prints the result directly, as required by the 
problem statement.

Example:
Input: [1, 3, 5, 7, 9]
Output: 16 24

'''

def miniMaxSum(arr):
	# Write your code here
	min_list = arr[:]
	max_list = arr[:]
	min_sum = 0
	max_sum = 0
    
	for i in range(4):
		current_min = min(min_list)
		current_max = max(max_list)
        
		min_sum += current_min
		max_sum += current_max
        
		min_list.remove(current_min)
		max_list.remove(current_max)
        
		# print(f"Vuelta: {i}")
		# print(f"min_sum: {min_sum}")
		# print(f"max_sum: {max_sum}")
		# print(f"min_list: {min_list}")
		# print(f"max_list: {max_list}")
        
	print(f"{min_sum} {max_sum}")

	# Solution approach summary:
	# This implementation creates two copies of the input list. In four iterations, it removes the smallest 
    # element from one copy and the largest element from the other, accumulating their sums. This guarantees 
    # the minimum and maximum possible sums by always selecting the four smallest and four largest values, 
    # respectively. The result is printed as required by the problem statement.
