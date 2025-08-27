# Copy here code of line function from previous exercise
def line(length, character):
    if character != "":
        print(length*character[0])
    else:
        print(length*"*")

def square_of_hashes(size):
    # You should call function line here with proper parameters
    height = size
    while height > 0:
        line(size, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
