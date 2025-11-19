"""
Count how many times each element appears in a list.
Input: [1, 2, 2, 3] → Output: {1: 1, 2: 2, 3: 1}
"""

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

print("Data analysis started:")

data = {}
target = number_list[0]
data[target] = 0

# Adding keys to data
for number in range(1, len(number_list)): # Remember that range doesn't include the last value.
    if number_list[number] != target:
        target = number_list[number]
        data[target] = 0

# Modyfing occurences 
for key in data:
    for number in number_list:
        if key == number:
            data[key] += 1 # Increasing the ocurrences of that key

# Showing the final results
print(data)
    

# Solution 2: 
data2 = {}
for number in number_list:
    if number in data2:
        data2[number] += 1 # Adds the ocurrence
    else:
        data2[number] = 1 # Creates the key and add one occurence


"""
Notes:
- Variables defined inside a loop or block in Python are accessible outside the block.
- The for loop 'for number in range(1, len(number_list))' does not go out of range because range stops at len(number_list) - 1.
- Your current approach works regardless of whether repeated numbers are grouped or separated in the list, because you count occurrences for each key afterwards.
- A more robust and Pythonic way is to use a dictionary to count occurrences (see Solution 2), or use collections.Counter.
- Both alternatives work regardless of the order of elements in the list.

Efficiency:
- The first solution (nested loops: for key in data, for number in number_list) has O(n^2) time complexity, where n is the length of the list. For each unique key, you iterate through the entire list to count occurrences.
- The second solution (single loop with dictionary) has O(n) time complexity, because each element is processed once and dictionary operations (insert/update) are O(1) on average.
- For large lists, the second solution is much more efficient.
"""