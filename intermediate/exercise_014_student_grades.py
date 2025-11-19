"""
Student Grades (listas + dicts)

Given a list of students like:

[
    {"name": "Alice", "grades": [8, 7, 9]},
    {"name": "Bob", "grades": [6, 6, 7]}
]

Return:
 Each students average
 Which student has the highest average

"""

students = [
    {"name": "Alice", "grades": [8, 7, 9]},
    {"name": "Bob", "grades": [6, 6, 7]},
    {"name": "Charlie", "grades": [9, 8, 10]},
    {"name": "Diana", "grades": [5, 7, 6]},
    {"name": "Eve", "grades": [10, 10, 9]},
    {"name": "Frank", "grades": [7, 6, 8]},
    {"name": "Grace", "grades": [8, 8, 8]},
    {"name": "Hank", "grades": [6, 5, 7]},
    {"name": "Ivy", "grades": [9, 9, 8]},
    {"name": "Jack", "grades": [7, 8, 7]}
]

def avg(nums: list[int]) -> float:
    result = 0
    for num in nums:
        result += num
    return round(result/(len(nums)), 2)

def data_analysis(students: list[dict[str, str | list[int]]]) -> tuple[dict[str, float], list[str, float]]:
    results = ({},["", 0.0])

    for student in students:
        name = student["name"]
        average = avg(student["grades"])
        results[0][name] = average
        
        if results[1][1] < average:
            results[1][1] = average
            results[1][0] = name

    return results

print(data_analysis(students))

"""
Notes:
- The function calculates each student's average and stores them in a dictionary.
- It tracks the student with the highest average using a mutable list, then (optionally) converts it to a tuple before returning.
- The averages are rounded to two decimal places.
- The return type should be tuple[dict[str, float], tuple[str, float]] for clarity and immutability.
- Time complexity is O(n), where n is the number of students.
"""

# Solution 2 (OOP)

class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def average(self) -> float:
        return round(sum(self.grades) / len(self.grades), 2)

students = [
    Student("Alice", [8, 7, 9]),
    Student("Bob", [6, 6, 7]),
    # ...
]

averages = {student.name: student.average() for student in students}
best = max(students, key=lambda student: student.average())
print(averages)
print(f"Best: {best.name} ({best.average()})")

"""
Notes:
- This solution uses an object-oriented approach with a Student class.
- Each student is represented as an object with 'name' and 'grades' attributes, and an 'average' method to compute their average grade.
- A dictionary comprehension is used to build a mapping of student names to their averages.
- The built-in max() function with a lambda is used to find the student with the highest average.
- This approach is more structured and readable, especially for larger or more complex data.
- Time complexity is O(n), where n is the number of students.
"""
