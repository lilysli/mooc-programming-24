def everything_reversed(wordlist : list) -> list:
    newlist = []
    for word in wordlist:
        newlist.append(word[::-1])
    return newlist[::-1]

if __name__ == "__main__":
    new_list = everything_reversed(my_list)
    print(new_list)