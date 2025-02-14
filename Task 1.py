def print_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

rows = 5
print_pyramid(rows)
