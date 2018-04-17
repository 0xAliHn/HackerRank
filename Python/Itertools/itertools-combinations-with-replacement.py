from itertools import combinations_with_replacement

S, k = input().split()

print(*[''.join(i) for i in combinations_with_replacement(sorted(S), int(k))], sep='\n')
