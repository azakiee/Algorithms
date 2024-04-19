def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def fib_din(n):
    if n >= len(fib_list):
        for i in range(len(fib_list), n + 1):
            fib_list.append(fib_din(n-1)+ fib_din(n-2))
    return fib_list[n]


fib_list = [0, 1]


for i in range(100):
    print(i, fib_din(i))