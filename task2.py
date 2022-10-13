
def game():
    n = int(input('Колличество конфет - '))
    player = False
    while n > 0:
        print(f"\t-Xод {int(player) + 1} игрока-")
        turn = int(input('Введите число: '))
        while not 0 < turn < 29:
            turn = int(input('Введите число: '))
        n -= turn
        player = not player
        print(f"осталось {n} конфет")
    print("Победил " + str(int(not player) + 1) + " игрок")


game()
