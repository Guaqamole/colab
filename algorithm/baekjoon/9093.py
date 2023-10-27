n = int(input())
answer = [input().split() for _ in range(n)]

for words in answer:
    for word in words:
        print(word[::-1], end=" ")
        
        ## use stack... idiot.