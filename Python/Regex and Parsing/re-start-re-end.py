import re
s, p = input(), input()
pattern = re.compile(p)
m = pattern.search(s)
if m:
    while m:
        print('({}, {})'.format(m.start(), m.end()-1))
        m = pattern.search(s, m.start()+1)
    
else:
    print('({}, {})'.format(-1, -1))
