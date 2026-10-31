# Write a program that searches for a number in a list and breaks the loop when found
numbers = [10, 20, 30, 40, 50]
for i in numbers:
    if i == 30:
        print("Number found")
        break