import sys
from datetime import datetime as dt

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = dt.strptime(t1, fmt)
    t2 = dt.strptime(t2, fmt)
    return int(abs((t1-t2).total_seconds()))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
