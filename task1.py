"""
  1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

"""

with open("5.2", "r", encoding="utf-8") as f:
    text = f.read().split()
    lst = list(filter(lambda x: not x.find("абв") != - 1, text))

with open("5.2", "w", encoding="utf-8") as f:
    for i, item in enumerate(lst):
        f.write(str(item) + " ")
