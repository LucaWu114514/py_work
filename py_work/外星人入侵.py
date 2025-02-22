from random import randint
class Alieninvasion:
    input('press enter to start game!')
    kill_number = 0
    while True:
        if kill_number <= 1:
                    alien = 'alien'
        elif kill_number >= 1:
                    alien = 'aliens'
        randint_number = randint(1,5)
        anser = input('Do you want to kill aliens?')
        yes = 'yes'
        no = 'no'
        if anser == yes:
            if randint_number == 1 or randint_number == 2 or randint_number == 3 or randint_number == 4:
                print('You kill an alien')
                kill_number += 1
            elif randint_number == 5:
                input('You kill no alien')
                input('Now it fights with you!')
                input('Your gun was break!')
                new_anser = input('run or fight?')
                if new_anser == 'run':
                    input('You run away,you have a new gun now!')
                    continue
                elif new_anser == 'fight':
                    dead = randint(1,2)
                    if dead == 1:
                        print('You win,you have anew gun now!')
                        kill_number += 1
                        continue
                    elif dead == 2:
                        input('You dead!')
                        input(f'You kill {kill_number} {alien}')
                        break
                else:
                      print('?')
                      print('Game over')
                      break
        elif anser == no:
                print('Oh!What a pity!')
                print(f'You kill {kill_number} {alien}')
                break
        else:
            print('?')
            print('Game over')
            break    
