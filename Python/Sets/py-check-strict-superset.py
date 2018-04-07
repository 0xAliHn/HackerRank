A = set(input().split())
result = True
for _ in range(int(input())):
    if not A.issuperset(set(input().split())):
        result = False
        break
    
print(result)
