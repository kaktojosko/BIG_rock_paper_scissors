# РАБОТАЕТ ОКЕЙ
import random
ex = False
name = input('Enter your name: ')
print('Hello,', name)
score1 = 0
# Пустой ввод = камень, ножницы и бумага в игре
# Ввод из rock, paper даст все 15 игровых фигур
moves = [x for x in input().split(',')]

print("Okay, let's start")
winning_cases = {
    'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
}

losing_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

# РАБОТАЕТ ОКЕЙ
with open('rating.txt', 'a+') as file:
    file.seek(0)
    lines = file.readlines()
    for line in lines:
        if line.startswith(name):
            score1 = int(line[len(name) + 1:])


# РАБОТАЕТ ОКЕЙ
def check_name(name):
    exists = False
    with open('rating.txt', 'a+') as file:
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            if name in line:
                exists = True

        if not exists:
            file.seek(0)
            file.write(name + ' ' + str(score1) + '\n')


check_name(name)


# РАБОТАЕТ ОКЕЙ
def rating(z):
    with open('rating.txt', 'a+') as file:
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            if line.startswith(z):
                print('Your rating:', score1)


# РАБОТАЕТ ОКЕЙ
def ez_win(x):
    if len(moves) == 1:
        win = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
        print('Sorry, but the computer chose ' + win[x])
    else:
        print('Sorry, but the computer chose ' + random.choice(losing_cases[x]))


# РАБОТАЕТ ОКЕЙ
def ez_lose(x):
    global score1
    if len(moves) == 1:
        lose = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        loser: str = lose[x]
        print('Well done. The computer chose {} and failed'.format(loser))
    else:
        print('Well done. The computer chose {} and failed'.format(random.choice(winning_cases[x])))
    score1 += 100
    change_score()


# РАБОТАЕТ ОКЕЙ
def draw(x):
    global score1
    tie = {'rock': 'rock', 'scissors': 'scissors', 'paper': 'paper', 'water': 'water', 'dragon': 'dragon',
           'devil': 'devil',
           'gun': 'gun', 'fire': 'fire', 'snake': 'snake',
           'human': 'human', 'tree': 'tree', 'wolf': 'wolf', 'sponge': 'sponge',
           'air': 'air', 'lightning': 'lightning'
           }
    print('There is a draw ({})'.format(tie[x]))
    score1 += 50
    change_score()


# РАБОТАЕТ ОКЕЙ
def mainloop(y):
    global ex, name
    r_int = random.randint(1, 3)
    if r_int == 1 and y in winning_cases and y != '!exit':
        ez_win(y)
    elif r_int == 2 and y in winning_cases and y != '!exit':
        ez_lose(y)
    elif r_int == 3 and y in winning_cases and y != '!exit':
        draw(y)
    elif y == '!exit':
        print('Bye!')
        ex = True
    elif y == '!rating':
        rating(name)
    else:
        print('Invalid input')


# РАБОТАЕТ ОКЕЙ
def change_score():
    global name, score1
    with open('rating.txt', 'a+') as f2:
        f2.write(name + ' ' + str(score1))
    with open('rating.txt', 'w+') as f2:
        counter = 0
        lines = f2.readlines()
        for line in lines:
            if line.startswith(name) and counter < 1:
                line = ''
                counter += 1
        f2.write(name + ' ' + str(score1))


# РАБОТАЕТ ОКЕЙ
while ex is False:
    player_move = input().lower()
    mainloop(player_move)
