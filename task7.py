def f(x):
    if x < 3:
        return 1
    if x > 2:
        return sum(f(i) for i in range(1, x))


print(f(18))