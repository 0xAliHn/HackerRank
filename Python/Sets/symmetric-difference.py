m, s1 =(input(), set(input().split()))

n, s2 = (input(),set(input().split()))

### Short form of above code in a single line
# a, b = [set(input().split()) for _ in range(4)][1::2]

print(*sorted(s1^s2, key=int), sep='\n')
