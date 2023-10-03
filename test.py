from random import randint

money = 10

while money > 0:
    input('нажмите ENTER чтобы продолжить')
    player_1 = randint(2, 12)
    player_2 = randint(2, 12)

    print ('вы выбросили число', player_1)
    print ('компьютер выбросил число', player_2)

    if player_1 > player_2:
        money += 1
        print('вы победили')
        print('у вас', money, 'монет')
    elif player_1 < player_2:
        print('победил компьютер')
        money -= 1
        print(money)
    else:
        print('Ничья')
print(money)

