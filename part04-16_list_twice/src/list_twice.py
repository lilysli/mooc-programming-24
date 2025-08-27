itemlist = []

while True:
    item = int(input("New item:"))
    if item == 0:
        print("Bye!")
        break
    itemlist.append(item)
    print(f"The list now: {itemlist}")
    print(f"The list in order: {sorted(itemlist)}")
