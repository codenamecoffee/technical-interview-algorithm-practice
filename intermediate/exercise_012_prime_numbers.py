from math import sqrt

"""
Prime Numbers (loops + functions)

Write a function that returns all prime numbers up to n.
"""

while True:
    try:
        n = int(input("Please, enter an integer greater than 1: "))
        if n > 1:
            break
        else:
            print("The number must be greater than 1.")
    except ValueError:
        print("Please, enter a valid integer.")

def is_prime(num: int) -> bool:
    result = True
    divider = 2
    while divider <= sqrt(num) and num % divider != 0:
        divider += 1
    if divider != num:
        result = False
    return result


def prime_numbers(n: int) -> list[int]:
    result = []
    for i in range(2, n+1):
        if is_prime(i):
            print(f"\n{i}, es primo.")
            result.append(i)
        else:
            print(f"\n{i}, no es primo.")
        print(f"=> {result}")
    return result

print(f"\n=> Lista final: {prime_numbers(n)}\n")

"""
Notes:
- The solution uses a while loop with try-except to ensure the user enters an integer greater than 1.
- The is_prime function checks for primality by testing divisibility up to num.
- For efficiency, you can check divisibility only up to sqrt(num).
- The prime_numbers function collects all primes up to n using is_prime.
- Time complexity is O(n√n), which is acceptable for small n.
- Prints are included for debugging; remove them for a cleaner output.
"""