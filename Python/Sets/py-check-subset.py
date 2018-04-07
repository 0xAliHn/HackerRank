for i in range(int(input())):
    _, A = input(), set(input().split())    
    _, B = input(), set(input().split())
    print(A.issubset(B))
