from collections import namedtuple
n, a = int(input()), input()
total = 0
Student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
# use : for left allign and :> for rihgt allign
print('{:.2f}'.format(total/n))
