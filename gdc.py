a = int(input())
b = int(input())
def gdc(a,b):
    if b == 0:
        return a
    return gdc(b, a % b)

print(gdc(a,b))