from random import randint


computer = 0
player = 0
game ={
    's':'scissors',
    'p': 'paper',
    'r' : 'rock'
}
while True:
    inp = input('rock, paper, scissors: ')
    if inp not in ['r', 'p', 's']:
        print(f'not valid {inp}')
        continue
    print(f'player choice : {game[inp]}')
    choices = ['r','p','s']
    random_number = randint(0, 2)
    c = choices[random_number]
    print(f'computer choice:  {game[c]}')

    if inp == c:
        print('equal')
    elif inp == 's':
        if c == 'r':
            print('computer win')
            computer += 1
        else:
            print('plyer win')
            player += 1
    elif inp == 'p':
        if c == 's':
            print('computer win')
            computer += 1
        else:
            print('plyer win')
            player += 1
    elif inp == 'r':
        if c == 'p':
            print('computer win')
            computer += 1
        else:
            print('plyer win')
            player += 1
    print('<_____________________>')       
    print(f'total score plyer: {player}')
    print(f'total score computer: {computer}')
    print('<_____________________>')

    if computer == 3:
        print('computer winner')
        break
    if player == 3:
        print('You winner')
        break