"""
Return both the smallest and largest numbers in a list.
Input: [4, 7, 2, 9] → Output: (2, 9)
"""
# Using the a part from the last exercise:

number_list = []
stop = False

while not stop:
    try:
        number = int(input("\nPlease, add a number to the list (can be repeated): "))
    except ValueError:
        print("You did not enter an int number. Try again.")
        continue  # Ask again

    number_list.append(number)
    print("\nThe number list until now looks like this: ")
    print(number_list)

    while True:
        option = input("\nDo you wanna still adding new numbers to the list? (y/n): ")
        match option.lower():
            case "y":
                break
            case "n":
                stop = True
                break
            case _:
                print("Invalid option.")

print("\nThe result list looks like this:")
print(f"{number_list}\n")

# Data analysis
min_value = number_list[0]
max_value = number_list[0]

for number in range(1, len(number_list)):
    if number_list[number] > max_value:
        max_value = number_list[number]
    if number_list[number] < min_value:
        min_value = number_list[number]

print(f"\n=> min_value: {min_value}, max_value: {max_value} .")

# Solution 2 (Pythonic)

min_value2 = min(number_list)
max_value2 = max(number_list)

print(f"\n=> min_value: {min_value}, max_value: {max_value} .")

"""
Notes:
- This solution iterates through the list once to find both the minimum and maximum values, so its time complexity is O(n), where n is the length of the list.
- Using the built-in min() and max() functions is more Pythonic and equally efficient (O(n) each).
- For very large lists, using min() and max() separately is still O(n) overall, since constants are ignored in Big O notation.
- Both approaches are valid and efficient for this problem.
"""