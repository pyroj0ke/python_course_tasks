numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(lambda x: x % 2 == 1 and x > 50, numbers)))