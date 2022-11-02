# Задача - Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'

# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')

# Задача №38: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# вариант человек против бота:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

   
      # Создайте программу для игры в ""Крестики-нолики"".

print('*'*100)
print('\n')
print('А теперь давайте сыграем в крестики нолики!')

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

# design_board(board)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуй')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Победила, ДРУЖБА)')
        design_board(board)
game(board)


# Задача №41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W



def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")