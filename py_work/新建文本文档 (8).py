from random import randint

real_bullet = randint(1,6)
money = 0
bullet_number = 6
fire = 1
while True:

    ask = input('shut(1)not shut(2)over(3)')
    ask = int(ask)
    if ask == 1:
        if fire == real_bullet:
            print('You dead')
            money = 0
            print('You get no money.')
            print('Again')
            fire = 1
            bullet_number = 6
            real_bullet = randint(1, 6)
        elif bullet_number == 2:
            print(f'You get {money + 1000}$')
            print('Again')
            fire = 1
            bullet_number = 6
            real_bullet = randint(1, 6)
        else:
            print('Lucky you')
            money = money + 1000
            bullet_number = bullet_number - 1
            fire = fire + 1

    elif ask == 2:
        
        print(f'You get {money} $.')
        print('Again')
        fire = 1
        bullet_number = 6
        real_bullet = randint(1,6)
    elif ask == 3:
        print(f'You get {money} $.')
        break
