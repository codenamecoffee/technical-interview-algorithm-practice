"""
### Plus Minus Ratios

Given a list of integers, the task is to determine the proportion of elements that are positive, negative, and equal to zero.

For each category, the ratio is calculated by dividing the number of occurrences by the total number of elements in the list.  
The results must be printed with exactly six digits after the decimal point, each on a separate line, following this order:

1. Positive values ratio  
2. Negative values ratio  
3. Zero values ratio  

Example: arr = [1, 1, 0, -1, -1] There are n=5 elements. two positive, two negative and one zero. 
Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. 

Results are printed as: 

    0.400000 
    0.400000 
    0.200000

This exercise focuses on basic iteration, conditional logic, and numeric formatting with fixed precision.

### Notes

- The input list always contains at least one element.
- Values may be positive, negative, or zero.
- Output precision is important: results must be formatted to six decimal places.
- The function prints the results directly and does not return any value.

"""

# Solution:

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for number in arr:
        if number > 0:
            positive += 1
        elif number == 0:
            zero += 1
        else:
            negative += 1

    print(f"{positive / len(arr):.6f}")
    print(f"{negative / len(arr):.6f}")
    print(f"{zero / len(arr):.6f}")


"""
### Solution Overview

The solution iterates once over the input list and counts how many elements fall into each category: positive, negative, and zero.

After counting:
- Each count is divided by the total number of elements to obtain the ratio.
- The results are printed using fixed-point formatting with six decimal places.

This approach runs in linear time **O(n)** and uses constant extra space **O(1)**.

----

### Final Remarks

While this problem is trivial in Python due to its built-in support for iteration and numeric formatting, the same task would require more verbose code in lower-level languages such as C or C++, where manual formatting and type handling are necessary.

The exercise demonstrates attention to detail, especially regarding output precision, which is a common requirement in technical assessments.

"""
