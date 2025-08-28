def read_fruits():
    fruits = {}
    with open("fruits.csv") as f:
        for line in f:
            name, price = line.strip().split(";")
            fruits[name] = float(price)
    return fruits
