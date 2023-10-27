n = int(input())
answer = [input() for _ in range(n)]

for pair in answer:
    for _ in range(len(pair)):
        pair = pair.replace('()', '')
    if pair:
        print("NO")
    else:
        print("YES")