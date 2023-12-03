import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Загадайте число від 1 до {x}: '))
        if guess < random_number:
            print('Вибачте, вгадайте ще раз. Число більше.')
        elif guess > random_number:
            print('Вибачте, вгадайте ще раз. Число менше.')

    print(f'Вітаю, Ви вгадали число {random_number} правильно!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  
        feedback = input(f'Чи {guess} занадто високе (H), занадто низьке (L) чи правильне (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Комп\'ютер вгадав ваш номер, {guess}, правильно!')


guess(10)