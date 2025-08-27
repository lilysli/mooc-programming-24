def list_of_stars (numberlist : list):
    for number in numberlist:
        print(number*"*")

if __name__ == "__main__":
    list_of_stars([3,7,1,1,2])