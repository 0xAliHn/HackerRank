n, x = map(int, input().split())
A = []
for _ in range(x):
    A.append(list(map(float, input().split())))

for i in zip(*A): 
    print(sum(i)/x)
