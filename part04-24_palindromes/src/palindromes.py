def palindromes(word : str) -> bool:
    return list(word) == list(reversed(word))

while True:
    word = input("Please type in a palindrome:")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
