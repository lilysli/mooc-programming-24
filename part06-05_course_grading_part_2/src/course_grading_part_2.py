students = {}

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

def calc_exercise_points(exercises : int) -> int:
    return int(exercises/4)

def calc_grade(points : int) -> int:
    if points >= 0 and points < 15:
        return 0
    elif points >= 15 and points < 18:
        return 1
    elif points >= 18 and points < 21:
        return 2
    elif points >= 21 and points < 24:
        return 3
    elif points >= 24 and points < 28:
        return 4
    else:
        return 5

with open(student_info) as student_file:
    for line in student_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        student_number = parts[0]
        name = parts[1] + " " + parts[2].strip()
        students[student_number] = [name]

with open(exercise_data) as exercise_file:
    for line in exercise_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        student_number = parts[0]
        exercise_list = [int(p.strip()) for p in parts[1:]]
        students[student_number].append(exercise_list)
        exercise_points = calc_exercise_points(sum(exercise_list))
        students[student_number].append(exercise_points)


with open(exam_data) as exam_file:
    for line in exam_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        student_number = parts[0]
        exam_points = [int(p.strip()) for p in parts[1:]]
        total_points = sum(exam_points) + students[student_number][2]
        students[student_number].append(calc_grade(total_points))

for key, value in students.items():
    print(f"{value[0]} {value[3]}")