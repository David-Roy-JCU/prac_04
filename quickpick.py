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
        print("{} random is {}".format(x + 1, number))
        if number not in numbers:
            numbers.append(number)
            print("appended by the if loop", str(number))
        else:
            while number in numbers:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(number)
            print("derived from the while loop", str(number))

    print(sorted(numbers))
print()


    # numbers = [numbers.append(randint(MIN_NUMBER - 1, MAX_NUMBER)) for number in numbers if number not in numbers]
    # print(numbers)
