cnt = 0
def makeone(n):
    global cnt
    if n == 1:
        return 1
    elif n % 3 == 0:
        cnt += 1
        return makeone(n/3)
    elif n % 2 == 0:
        cnt += 1
        return makeone(n/2)
    else:
        cnt += 1
        return makeone(n-1)

print(makeone(10), cnt)