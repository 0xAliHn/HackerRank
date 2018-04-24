import sys
from collections import OrderedDict
import operator

if __name__ == "__main__":
    s = input().strip()
    
ordered_dict = OrderedDict()
    
for i in range(len(s)):
    ordered_dict[s[i]] = ordered_dict.get(s[i],0)+1
    
lis = sorted(sorted(ordered_dict.items()), key=operator.itemgetter(1), reverse=True)
for i in range(0,3):
    print(*lis[i])
