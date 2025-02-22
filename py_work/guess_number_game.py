
from random import randint

computer_guess = randint(1, 100)
while True:

            answer = input('guess number 1-100')
            try:
                answer = int(answer)

            except ValueError:
                print('must a number')
                continue

            if computer_guess > answer:
                    print('low')
            elif computer_guess < answer:
                    print('high')
            elif computer_guess == answer:
                    print(bool(computer_guess == answer))
