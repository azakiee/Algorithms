a = int(input())
n = int(input())
def pow(a,n):
    print(f"Возвожу {a} в степень {n}")
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(a*a, n//2)
    if n % 2 == 1:
        return a * pow(a, n - 1)
print(pow(a,n))