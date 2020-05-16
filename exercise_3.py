n = int(input('enter a number'))
for i in range(1, n + 1):
    print()  # for new line
    for j in range(0, i):
        print('*', end='')
