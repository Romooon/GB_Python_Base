from itertools import cycle, count

my_list = ['Python', 'the', 'best', 'for', 'us']

c = 0
for el in cycle(my_list):
    if c >= 40:
        break
    print(el)
    c += 1

for el in count(5, 1):
    if el > 35:
        break
    print(el)
