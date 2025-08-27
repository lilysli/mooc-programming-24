itemlist = []
count = 0
print(f"The list is now {itemlist}")

while True:
    choice = input("a(d)d, (r)emove or e(x)it:").lower()

    if choice == "d":
        count += 1
        itemlist.append(count)
    elif choice == "r":
        count -= 1
        itemlist.pop(len(itemlist)-1)
    elif choice == "x":
        print("Bye!")
        break
    else:
        print("This is not a valid option")
    print(f"The list is now {itemlist}")
