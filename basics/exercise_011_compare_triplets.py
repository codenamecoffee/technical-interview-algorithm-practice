"""
Problem Summary (adapted from HackerRank):

Alice and Bob each propose a challenge that is evaluated in three categories:
clarity, originality, and difficulty. Each category is rated with an integer 
between 1 and 100.

You are given two triplets:
- a = [a0, a1, a2] → Alice's scores
- b = [b0, b1, b2] → Bob's scores

Your task is to compare each corresponding category:

- If a[i] > b[i], Alice earns 1 point.
- If a[i] < b[i], Bob earns 1 point.
- If a[i] == b[i], no points are awarded.

The function must return an array of length 2:
[result_for_Alice, result_for_Bob]

Example:
a = [5, 6, 7]
b = [3, 6, 10]
Output → [1, 1]
"""

def compareTriplets(a, b):
    result = [0, 0]
    
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
        else: 
            continue

    return result


# Solution N°2 (Pythonic)

def compareTriplets(a, b):
    alice = sum(x > y for x, y in zip(a, b))
    bob   = sum(x < y for x, y in zip(a, b))
    return [alice, bob]


"""
This solution also works because:

- True it's evaluated as 1
- False it's evaluated as 0


Summary:

Both solutions run in constant time O(1) since the input size is fixed (three categories).
The Pythonic version leverages zip and generator expressions for concise code.
The logic would also work for longer lists, but the problem specifies triplets.

** Note: 

zip(a, b) creates an iterator that aggregates elements from both lists (a and b) in pairs.

For example:

if a = [5, 6, 7] and b = [3, 6, 10], zip(a, b) produces: (5, 3), (6, 6), (7, 10)

This allows you to compare corresponding elements from both lists in a single loop.
If the lists have different lengths, zip stops at the shortest one, ignoring extra elements.

"""