"""
Interval Merger

Concepts: sorting, greedy algorithms, data structure manipulation

Given a list of intervals [start, end], merge all overlapping intervals.

Input:
[[1, 3], [2, 6], [8, 10], [15, 18]]

Output:
[[1, 6], [8, 10], [15, 18]]

Rules:
- If intervals do not overlap, keep them separate.
- If intervals overlap, merge them by taking:
  start = min(start1, start2)
  end = max(end1, end2)

Requires: sorting + merging logic.

"""

user_input = [[1, 3], [2, 6], [8, 10], [15, 18]]

def merger(interval_1: list[int,int], interval_2: list[int,int]) -> list[int,int]:
    return [min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1])]

def interval_merger (interval_list: list[list[int,int]]) -> list[list[int,int]]:
    if not interval_list:
        print("The list is empty.")
        return []

    ordered_intervals = sorted(interval_list) # The intervals may not be in order
    result = [ordered_intervals[0]]

    for current in ordered_intervals[1:]:
        last = result[-1] # Last element of the list.
        if last[1] >= current[0]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)

    return result

print(interval_merger(user_input))


"""
Notes:
- The function first sorts the list of intervals by their start value to ensure correct merging.
- It iterates through the sorted intervals, comparing each to the last merged interval.
- If the current interval overlaps with the last one, they are merged by updating the end value.
- If there is no overlap, the current interval is added as a new entry in the result.
- This approach ensures all overlapping intervals are merged in a single pass.
- Time complexity is O(n log n) due to sorting, and O(n) for the merging pass.
- The solution is efficient, clear, and handles all edge cases.
"""