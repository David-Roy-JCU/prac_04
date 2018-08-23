"""
Quick Pick lottery ticket generator

"""
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_games = int(input("How many Quick Picks? "))

for i in range(number_of_games):
    numbers = []
    # generate the list of 6 unique random numbers
    for x in range(6):
        numbers.append(randint(MIN_NUMBER - 1, MAX_NUMBER))
    print(numbers)
print()


    # numbers = [random.randint(number) for number in range(6)]
    # print(numbers)
