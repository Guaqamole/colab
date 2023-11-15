n = int(input())
tab = [0] * 1001
tab[1], tab[2] = 1,2

for i in range(3, n+1):
    tab[i] = (tab[i - 1] + tab[i - 2]) % 10007

print(tab[n])