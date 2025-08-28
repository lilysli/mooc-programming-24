def largest():
    with open("numbers.txt") as new_file:
        largest = 0

        for line in new_file:
            number = int(line.strip())
            if number > largest:
                largest = number
        return largest
