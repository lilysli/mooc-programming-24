students = {}

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")


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
        students[student_number].append([int(p.strip()) for p in parts[1:]])

for key, value in students.items():
    print(f"{value[0]} {sum(value[1])}")
