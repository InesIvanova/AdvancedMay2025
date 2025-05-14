n = int(input())

student_records = {}

for _ in range(n):
    data = tuple(input().split())
    name = data[0]
    grade = float(data[1])

    if name not in student_records:
        student_records[name] = []
    student_records[name].append(grade)


for name, grades in student_records.items():
    avg_grade = sum(grades) / len(grades)
    grades_as_str = [f"{el:.2f}" for el in grades]
    print(f"{name} -> {' '.join(grades_as_str)} (avg: {avg_grade:.2f})")

