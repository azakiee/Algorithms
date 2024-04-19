def f(x):
    if x > 2:
        return f(x-1) * x + f(x-2) * (x-1)
    elif x == 2:
        return 3
    else:
        return x


print(f(5))