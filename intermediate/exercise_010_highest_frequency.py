"""
10. Highest Frequency

Given an array, return the most frequent value.
If there is a tie, return the smallest value.

def most_frequent(arr):
    pass
"""

user_input = input("Please, enter a list of numbers separated by commas (i.e. 3,-10,5,1,4,-4,70,..., etc): ")
nums_list = [int(x) for x in user_input.split(",")]

def most_frequent(arr: list[int]) -> int:
     
    if not arr:
        print("The list of numbers is empty.")
        return 0 
    
    data = {}
    for num in arr:
        if num in data:
            data[num] += 1
        else: 
            data[num] = 1

    print(data)
    
    max_value = max(data.values())

    keys = [x for x in data.keys() if data[x] == max_value]

    return min(keys)

print(f"The most frequent but smallest value of: \n-> {nums_list} is: {most_frequent(nums_list)}")

"""
Notes:
- The function counts the occurrences of each number using a dictionary.
- It finds the maximum frequency, then selects the smallest number among those with that frequency.
- Handles empty input gracefully.
- Make sure to convert input strings to integers before processing, otherwise comparisons may not work as expected.
- Time complexity is O(n), where n is the length of the input list.
- This approach is efficient and Pythonic for finding the most frequent (and smallest in case of a tie) value in a list.
"""