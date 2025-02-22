from random import randint

class AlienInvasion:
    def __init__(self):
        self.kill_number = 0

    def start_game(self):
        input('Press enter to start game!')
        while True:
            self.play_round()

    def play_round(self):
        alien = 'alien' if self.kill_number <= 1 else 'aliens'
        randint_number = randint(1, 5)
        answer = input('Do you want to kill aliens? (yes/no): ').strip().lower()
        
        if answer == 'yes':
            self.process_kill_attempt(randint_number, alien)
        elif answer == 'no':
            print(f'Oh! What a pity! You killed {self.kill_number} {alien}')
            print('Game over')
            return
        else:
            print('?')
            print('Game over')
            return

    def process_kill_attempt(self, randint_number, alien):
        if randint_number in [1, 2, 3, 4]:
            print('You killed an alien!')
            self.kill_number += 1
        elif randint_number == 5:
            print('You killed no alien. Now it fights with you! Your gun was broken!')
            self.process_fight_or_run()

        print(f'You have killed {self.kill_number} {alien}')

    def process_fight_or_run(self):
        new_answer = input('Run or fight? (run/fight): ').strip().lower()
        if new_answer == 'run':
            print('You ran away, you have a new gun now!')
        elif new_answer == 'fight':
            dead = randint(1, 2)
            if dead == 1:
                print('You win, you have a new gun now!')
                self.kill_number += 1
            else:
                print('You died!')
                print('Game over')

if __name__ == "__main__":
    game = AlienInvasion()
    game.start_game()
