a, b = map(int, input().split())

def euclid_gcd(n,m):
    if m == 0: 
        return n
    return euclid_gcd(m, n % m)

print(euclid_gcd(a,b))
print((a*b)//euclid_gcd(a,b))