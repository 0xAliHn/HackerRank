from itertools import combinations

S, k = input().split()

for i in range(1, int(k)+1):
    print(*[''.join(j) for j in combinations(sorted(S), i)], sep='\n')
