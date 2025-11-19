"""
Given an integer, print "Even" if it’s even, or "Odd" otherwise.
"""

number = int(input("Please, enter a number (to determine whether its 'Even' or 'Odd'): "))

if number % 2 == 0:
    print("The entered number is Even")
else:
    print("The entered number is Odd")

"""
Notes:
- The modulo operator (%) returns the remainder of the division.
- If number % 2 == 0, the number is even; otherwise, it is odd.
- This is the standard and Pythonic way to check for even or odd numbers.
- Using input() allows the user to test with different values.

- The time complexity of this program is O(1) (constant time), because the number of operations does not depend on the input value.
- Regardless of the number entered by the user, the program performs a fixed number of steps: reading input, checking parity, and printing the result.
- There are no loops or recursive calls, so the execution time remains constant.
"""