def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    
if __name__ == "__main__":
    n = 8
    memo = [0] * (n + 1)
    print(fibo(n))