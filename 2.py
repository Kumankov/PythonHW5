# Создайте программу для игры в ""Крестики-нолики"".
import os
clear = lambda: os.system('cls')
move=[0]*1000
moves = []
moveSimbol = ['(крестик)','(нолик)']
line = [0]*3
line[0] = [' ',' ',' ']
line[1] = [' ',' ',' ']
line[2] = [' ',' ',' ']
for i in range(len(move)):
    move[i] = input(f'ход {i%2+1} игрока {moveSimbol[i%2]} (введите координаты вида 1 2 через пробел - ').split()
    while int(move[i][0]) not in [1,2,3] or int(move[i][1]) not in [1,2,3]:
        print('Некорректный ход. Координаты должны быть от 1 до 3.')
        move[i] = input(f'ход {i%2+1} игрока {moveSimbol[i%2]} (введите координаты вида 1 2 через пробел - ').split()
    while move[i] in moves:
        print('такой ход уже был')
        move[i] = input(f'ход {i%2+1} игрока {moveSimbol[i%2]} (введите координаты вида 1 2 через пробел - ').split()
    moves.append(move[i])
    if not i%2:
        line[int(move[i][0])-1][int(move[i][1])-1] = 'X'
    elif i%2:
        line[int(move[i][0])-1][int(move[i][1])-1] = '0'        
    clear()
    print(f'{line[0][0]} | {line[0][1]} | {line[0][2]}')
    print('_________')
    print(f'{line[1][0]} | {line[1][1]} | {line[1][2]}')
    print('_________')
    print(f'{line[2][0]} | {line[2][1]} | {line[2][2]}')
    if i>3:
        if (line[0][0] == line[0][1] == line[0][2] == 'X'
            or line[1][0] == line[1][1] == line[1][2] == 'X'
            or line[2][0] == line[2][1] == line[2][2] == 'X'
            or line[0][0] == line[1][0] == line[2][0] == 'X'
            or line[0][1] == line[1][1] == line[2][1] == 'X'
            or line[0][2] == line[1][2] == line[2][2] == 'X'
            or line[0][0] == line[1][1] == line[2][2] == 'X'
            or line[0][2] == line[1][1] == line[2][0] == 'X'):
            print('Игрок 1 выиграл.')
            exit()
        elif (line[0][0] == line[0][1] == line[0][2] == '0'
            or line[1][0] == line[1][1] == line[1][2] == '0'
            or line[2][0] == line[2][1] == line[2][2] == '0'
            or line[0][0] == line[1][0] == line[2][0] == '0'
            or line[0][1] == line[1][1] == line[2][1] == '0'
            or line[0][2] == line[1][2] == line[2][2] == '0'
            or line[0][0] == line[1][1] == line[2][2] == '0'
            or line[0][2] == line[1][1] == line[2][0] == '0'):
            print('Игрок 2 выиграл.')
            exit()
        elif i == 8:
            print('Ничья. Игра окончена.')
            exit()




