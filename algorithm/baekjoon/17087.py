n, s = map(int, input().split())
a = list(map(int, input().split()))
diff = list(set(abs(a[i]-s) for i in range(n)))
d = min(diff)

def euclid_gcd(n,m):
    if m == 0: 
        return n
    return euclid_gcd(m, n % m)

for i in range(len(diff)):
    d = euclid_gcd(diff[i], d)
    
print(d)