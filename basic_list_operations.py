"""
intermediate exercises section 1.
"""

numbers = []

for i in range(5):
    new_number = int(input("Enter number: "))
    numbers.append(new_number)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average_of_numbers = sum(numbers) / len(numbers)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))
print()