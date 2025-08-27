# Copy here code of line function from previous exercise
def line(length, character):
    if character != "":
        print(length*character[0])
    else:
        print(length*"*")

def triangle(size):
    # You should call function line here with proper parameters
    count = 0
    while count <= size:
        line(count, "#")
        count += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
