cube = lambda x:pow(x,3)

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    ls = [0,1]
    for i in range(2,n):
        ls.append(ls[i-1]+ls[i-2])
    return ls
