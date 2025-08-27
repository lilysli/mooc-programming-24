def histogram(word : str):
    d = {}
    for letter in word:
        if letter not in d:
            d[letter] = "*"
        else:
            d[letter] += "*"
    for key, value in d.items():
        print(f"{key} {value}")

