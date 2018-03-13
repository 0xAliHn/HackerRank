from collections import defaultdict
if __name__ == '__main__':
    students_by_score = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_by_score[score].append(name)

second_lowest_score = sorted(students_by_score)[1]
for name in sorted(students_by_score[second_lowest_score]):
    print(name)
