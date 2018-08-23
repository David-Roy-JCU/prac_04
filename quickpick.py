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
        number = randint(MIN_NUMBER, MAX_NUMBER + 1)
        print("first rand is {}".format(number))
        if number not in numbers:
            numbers.append(number)
            print("from the if loop", str(number))
        else:
            number = randint(MIN_NUMBER, MAX_NUMBER + 1)
            print("Priming read is {}".format(number))
            while number not in numbers:
                numbers.append(number)
                number = randint(MIN_NUMBER, MAX_NUMBER + 1)
                print("from the while  loop", str(number))

        # numbers.append([(randint(MIN_NUMBER - 1, MAX_NUMBER)) for number in numbers if number not in numbers])
    print(numbers)
print()


    # numbers = [numbers.append(randint(MIN_NUMBER - 1, MAX_NUMBER)) for number in numbers if number not in numbers]
    # print(numbers)
