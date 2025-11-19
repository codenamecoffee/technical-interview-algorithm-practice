"""
Sum the digits of a number using recursion.
Input: 123 → Output: 6
"""

number = int(input("Please, enter a number (to add its digit into a total sum): "))

str_number = str(number) # Convert to string to manipulate it's digit individually.

def sum_digits(index: int):
    if index < 0:
        return 0
    else:
        return int(str_number[index]) + sum_digits(index - 1)

print(f"The digits of the number {number} added together result in: {sum_digits(len(str_number) - 1)}")

"""
Notes:
- This solution converts the input number to a string to access each digit individually.
- The recursive function sum_digits(index) sums the digits from right to left by decreasing the index.
- Base case: when index < 0, return 0.
- Recursive case: convert the current character to int and add it to the sum of the previous digits.
- The time complexity is O(d), where d is the number of digits in the number.
- An alternative approach is to use mathematical operations (modulo and integer division) to extract digits without converting to a string.
"""