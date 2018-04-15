if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lis = list(arr)
    z = max(lis)
    while max(lis) == z:
        lis.remove(z)
    print(max(lis))
