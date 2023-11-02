n = int(input())

def euclid_gcd(n,m):
    if m == 0: 
        return n
    return euclid_gcd(m, n % m)

for _ in range(n):
    answer = 0
    case = list(map(int, input().split()))
    for j in range(1,len(case)):
        for k in range(j+1,len(case)):
            answer += euclid_gcd(case[j],case[k])
    print(answer)