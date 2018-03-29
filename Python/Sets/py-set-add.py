s = set()

# Short way
[s.add(input()) for _ in range(int(input()))]

# More descriptive
#for _ in range(int(input())):
    #s.add(input())

print(len(s))
