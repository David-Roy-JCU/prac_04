"""
Quick Pick lottery ticket generator

"""
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_games = int(input("How many Quick Picks? "))

for i in range(number_of_games):
    numbers = []
    for x in range(6):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
        else:
            while number in numbers:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(number)
    numbers_sorted = sorted(numbers)
    for i in range(len(numbers_sorted)):
        print("{:>3}".format(numbers_sorted[i]), end = '')
    print()
