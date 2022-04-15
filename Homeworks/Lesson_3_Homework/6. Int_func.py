# def int_func(word):
#     return word.title()
#
# print(int_func('sunrise'))

# После разбора

def int_func(word):
    return word[0].upper() + word[1:].lower()

s = input('Введите слова: ').split()
for i, word in enumerate(s):
    if not word in enumerate(s):
        if not word.isascii() or not word.isalpha() or not word.lower():
            print('Ошибка!')
        else:
            s[i] = int_func(word)
print(' '.join(s))