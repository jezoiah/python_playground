"""
Problem 001: Find the Largest Number in a List

This program defines a function that finds and returns the largest number 
from a given list of integers without using Python's built-in max() or sorted() 
functions. The algorithm iterates through the list, compares each element, 
and keeps track of the current largest value.
"""

items = []
def find_largest(numbers: list[int]) -> int:
    maximum = numbers[0]
    for obj in numbers:
        if obj > maximum:
            maximum = obj
    return maximum

        
print("--- ONLY INTEGERS! ---")
arr = int(input("Enter the amount of items you want to add: "))
for i in range(1, arr + 1):
    num = int(input(f"Enter Item Number #{i}: "))
    items.append(num)

print(f"The largest number is: {find_largest(items)}")