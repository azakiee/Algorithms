a = int(input())
b = int(input())
def gdc(a,b):
    if a == b:
        return a
    elif a>b:
        return gdc(a-b,b)
    elif a<b:
        return gdc(a,b-a)
print(gdc(a,b))