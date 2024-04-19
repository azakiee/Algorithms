def f(x):
    if x > 1 and x % 2==1:
        return x + f(x-2)
    if x % 2 == 0:
        return x * f(x-1)
    elif x == 1:
        return 1


print(f(40))