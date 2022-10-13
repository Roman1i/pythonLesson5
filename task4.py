def zip_it():
    with open("source", "r") as file:
        letters = file.read()
    with open("result", "w") as file:
        count = 1
        for i, item in enumerate(letters):
            if i != len(letters) - 1:
                if letters[i] == letters[i+1]:
                    count += 1
                    if count == 9:
                        file.write(str(count) + item)
                        count = 0
                else:
                    file.write(str(count) + item)
                    count = 1
            else:
                if letters[i] == letters[i - 1]:
                    if count != 0:
                        file.write(str(count) + item)
                else:
                    file.write("1" + item)


def unzip_it():
    with open("source", "r") as file:
        letters = file.read()
    with open("result", "w") as file:
        for i, item in enumerate(letters):
            if not i % 2:
                file.write(int(item) * str(letters[i+1]))


print("Что делаем?\n1.Сжимаем\n2.Восстанавливаем\n")
func = input()
if func == "1":
    a = input("Введите набор символов: ")
    with open("source", "w") as file:
        file.write(a)
    zip_it()
    with open("result", "r") as file:
        print(file.read())
elif func == "2":
    a = input("Введите набор символов: ")
    with open("source", "w") as file:
        file.write(a)
    unzip_it()
    with open("result", "r") as file:
        print(file.read())
