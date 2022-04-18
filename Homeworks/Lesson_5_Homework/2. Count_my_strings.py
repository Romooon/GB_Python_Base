# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('Warrior.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, f'Слов в строке: {len(line.split())}', end='')
        print()
