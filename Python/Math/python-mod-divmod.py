a, b = int(input()), int(input())
#print(a//b)
#print(a%b)
#print(divmod(a,b))

# Single line solution
print('{0}\n{1}\n({0}, {1})'.format(*divmod(a,b)))
