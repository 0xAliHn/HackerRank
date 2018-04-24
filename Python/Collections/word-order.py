from collections import OrderedDict
ordered_dict = OrderedDict()

for i in range(int(input())):
    key = input()
    ordered_dict[key] = ordered_dict.get(key, 0) + 1

print(len(ordered_dict))
for k, v in ordered_dict.items():
    print(v, end=" ")
