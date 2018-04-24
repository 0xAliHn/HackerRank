from collections import deque
d = deque()

for _ in range(int(input())):
    cmd, *val = input().split()
    getattr(d, cmd)(*val)

print(*d)
