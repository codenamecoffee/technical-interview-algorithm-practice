"""
Given a list of integers, return the sum of all elements.
Example:
Input: [3, 5, 2] → Output: 10
"""

numbers = [10, 5 , 3 , 20, -3, 8]

total = 0 # Neutral element for addition

for number in numbers:
    total += number # O(1) per iteration

print(f"The numbers: {numbers} added together result in: {total}")

# Another way to solve the exercise:
total2 = sum(numbers)
print(f"Result using \"sum()\": {total2}")

"""
Comentarios:

- Using built-in names like 'input' or 'sum' as variable names is not recommended.
- It is necessary to initialize variables before using them.
- The "f" prefix in print() is called an f-string or "formatted string literal".
- They were not needed here, but there are things like "break" and "continue" which are
"control flow statements":

   ** break: exits the loop
   ** continue: skips to the next iteration of the loop

- **Note**: We did not check if the list was empty before operating with it.
(But i would pay attention to those details in more complex exercises).

Efficiency:

The algorithm is O(n), where n is the number of elements in the list.
Each addition is O(1), and you traverse the entire list once.

"""