# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if character != "":
        print(length*character[0])
    else:
        print(length*"*")


def shape(width, character, height, filler):
    tricount = 0
    while tricount <= width:
        line(tricount, character)
        tricount += 1
    while height > 0:
        line(width, filler)
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")