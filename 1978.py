n = int(input())
nums = map(int, input().split())
answer = 0

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for num in nums:
    if num == 1:
        pass
    elif num == 2 or is_prime(num):
        answer += 1

print(answer)