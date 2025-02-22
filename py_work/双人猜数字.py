
from random import randint

first_gamer = input("first_gamer what's your name?")
second_gamer = input("second_gamer what's your name?")
first_number = 1
second_number = 1
computer = randint(1,100)
while True:
    try:
        first_guess = input(f'{first_gamer} guess number')
        first_guess = int(first_guess)

        if first_guess == computer:
            print(f'{first_gamer.title()} is win.')
            print(f'{first_gamer.title()} guess {first_number} turn.')
            break
        elif first_guess <= computer:
            print('low!')
            first_number = first_number + 1
        elif first_guess >= computer:
            print('high!')
            first_number = first_number + 1
    except ValueError:
        print('only number')
        continue

    try:
        second_guess = input(f'{second_gamer} guess number')
        second_guess = int(second_guess)

        if second_guess == computer:
            print(f'{second_gamer.title()} is win.')
            print(f'{second_gamer.title()} guess {second_number} turns.')
            break
        elif second_guess <= computer:
            print('low!')
            second_number = second_number + 1
        elif second_guess >= computer:
            print('high!')
            second_number = second_number + 1
    except ValueError:
        print('only number')



