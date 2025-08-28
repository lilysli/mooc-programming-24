def oldest_person(people: list):
    oldest_person = people[0]
    for person in people:
        if person[1] < oldest_person[1]:
            oldest_person = person
    return oldest_person[0]


