def calc_exercise_points(exercises : int) -> int:
    return int(exercises/10)

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

total_points = 0
grades = []
total_pass = 0
total_fail = 0
stars = ["0: ", "1: ", "2: ", "3: ", "4: ", "5: "]

while True:
    value = input("Exam points and exercises completed: ")
    if value == "":
        print("Statistics:")
        print(f"Points average: {total_points/len(grades):.1f}")
        print(f"Pass percentage: {total_pass/(total_pass+total_fail)*(100):.1f}")
        print(f"Grade distribution:")
        for item in reversed(stars):
            print(f"{item}")
        break

    combined_points = value.split()
    exam_points = int(combined_points[0])
    exercise_points = calc_exercise_points(int(combined_points[1]))
    course_points = exam_points + exercise_points
    total_points += course_points
    if exam_points < 10:
        grade = 0
    else:
        grade = calc_grade(course_points)
    stars[grade] += "*"
    grades.append(grade)
    if grade == 0:
        total_fail += 1
    else:
        total_pass += 1

    


