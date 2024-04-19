def f(x):
    if x > 2:
        return f(x-1) - f(x-2) + 2 * x
    elif x == 2:
        return 2
    else:
        return x


print(f(6))