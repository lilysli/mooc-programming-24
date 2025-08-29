import urllib.request
import json
import ssl # add this library to your import section

def retrieve_all():
    # add the following line to the beginning of all your functions
    context = ssl._create_unverified_context()
    # the rest of your function
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses", context=context)
    courses = json.loads(my_request.read())
    enabled_courses = []

    for course in courses:
        if course["enabled"] == True:
            exercises = sum(course["exercises"])
            enabled_courses.append((course["fullName"], course["name"], course["year"], exercises))
    return enabled_courses

def retrieve_course(course_name: str):
    context = ssl._create_unverified_context()
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats", context=context)
    course = json.loads(my_request.read())
    weeks = len(course)
    students = max(week["students"] for week in course.values())
    hours = sum(week["hour_total"] for week in course.values())
    exercises = sum(week["exercise_total"] for week in course.values())
    hours_average = hours // students
    exercises_average = exercises // students

    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }

