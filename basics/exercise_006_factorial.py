"""
Implement a function that returns the factorial of a number.
Input: 5 → Output: 120
"""

def factorial(num: int):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

number = int(input("Please, enter a number (to calculate its factorial ): "))
print(f"The factorial of {number} (i.e., {number}!) is: {factorial(number)}")

"""
Notes:
- In Python, type hints are written as 'param: type', not 'type param'.
- The base case for factorial is 0! = 1.
- The function is recursive: it calls itself with num - 1 until num == 0.
- The time complexity is O(n), where n is the input number.
"""