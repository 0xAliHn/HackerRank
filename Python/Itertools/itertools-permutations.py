from itertools import permutations

S, k = input().split()

print(*[''.join(i) for i in permutations(sorted(S),int(k))], sep='\n')
