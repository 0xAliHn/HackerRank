k, l = int(input()), list(map(int, input().split()))
s = set(l)

print(((sum(s)*k)-(sum(l)))//(k-1))
