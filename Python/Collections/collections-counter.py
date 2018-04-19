from collections import Counter

_, shoes, noCus = int(input()), Counter(map(int, input().split())), int(input())

total = 0;
for i in range(noCus):
    size , price = map(int, input().split())
    if shoes[size]:
        total += price
        shoes[size] -= 1
        
print(total)
        
