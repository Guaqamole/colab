start, end = map(int, input().split())
answer = 0

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(start, end+1):
    if i == 1:
        pass
    elif i == 2 or is_prime(i):
        print(i)