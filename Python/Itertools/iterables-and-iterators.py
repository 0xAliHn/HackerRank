from itertools import combinations

_, s, k =int(input()), map(str, input().split()), int(input())

l = list(combinations(s, k))

f = [i for i in l if 'a' in i]
print(len(f)/len(l))
