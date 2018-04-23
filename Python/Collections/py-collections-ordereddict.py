from collections import OrderedDict
ordered_dictionary = OrderedDict()

for i in range(int(input())):
    key, _, val = input().rpartition(' ')
    ordered_dictionary[key] = ordered_dictionary.get(key, 0)+ int(val)
    
for i in ordered_dictionary.items():
    print(*i)
