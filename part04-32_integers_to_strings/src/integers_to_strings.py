def formatted(numbers : list) -> list:
    newlist = []
    for number in numbers:
        newlist.append(f"{number:.2f}")
    return newlist

if __name__ == "__main__":
    new_list = formatted(my_list)
    print(new_list)