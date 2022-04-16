def fact(n):
    for el in range(1, n+1):
        yield el

my_fact = 1
for el in fact(8):
    my_fact *= el

print(my_fact)