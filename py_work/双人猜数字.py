from random import randint

def get_guess(player_name):
    while True:
        try:
            guess = int(input(f'{player_name}, guess a number: '))
            return guess
        except ValueError:
            print('Please enter a valid number.')

def play_game():
    first_gamer = input("First gamer, what's your name? ")
    second_gamer = input("Second gamer, what's your name? ")
    computer_number = randint(1, 100)
    
    first_guess_count = 0
    second_guess_count = 0
    
    while True:
        first_guess = get_guess(first_gamer)
        first_guess_count += 1
        if first_guess == computer_number:
            print(f'{first_gamer.title()} wins! It took {first_guess_count} attempts.')
            break
        elif first_guess < computer_number:
            print('Too low!')
        else:
            print('Too high!')
        
        second_guess = get_guess(second_gamer)
        second_guess_count += 1
        if second_guess == computer_number:
            print(f'{second_gamer.title()} wins! It took {second_guess_count} attempts.')
            break
        elif second_guess < computer_number:
            print('Too low!')
        else:
            print('Too high!')

if __name__ == "__main__":
    play_game()
