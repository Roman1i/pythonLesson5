def output(lst):

    print(f'_{lst[0]}_|_{lst[1]}_|_{lst[2]}_\n'
          f'_{lst[3]}_|_{lst[4]}_|_{lst[5]}_\n'
          f'_{lst[6]}_|_{lst[7]}_|_{lst[8]}_')


def win_condition(lst):
    exits = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in exits:
        if lst[item[0]] == lst[item[1]] == lst[item[2]]:
            return lst[item[0]]
    return False


game_status = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
switch = 1

output(game_status)
while not win_condition(game_status):
    if switch == 1:
        print(f"Ход {switch}-го игрока (x).")
        xo = int(input("Введите позицию: "))
        game_status[xo - 1] = 'x'
        switch = 2
        output(game_status)
    elif switch == 2:
        print(f"Ход {switch}-го игрока (o).")
        xo = int(input("Введите позицию: "))
        game_status[xo - 1] = 'o'
        switch = 1
        output(game_status)

if switch == 1:
    switch = 2
    player = 'o'
elif switch == 2:
    switch = 1
    player = 'x'

print(f"Победил {switch}й игрок ({player})")
