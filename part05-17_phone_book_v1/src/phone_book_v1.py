def search(d : dict, name : str):
    if name in d:
        return d[name]
    else:
        return "no number"

def add(d: dict, name : str, number : str):
    d[name] = number
    return d

phonebook = {}
while True:
    selection = int(input("command (1 search, 2 add, 3 quit):"))
    if selection == 1:
        search_name = input("name:") 
        print(search(phonebook,search_name))
    elif selection == 2:
        add_name = input("name:")
        add_number = input("number:")
        phonebook = add(phonebook, add_name, add_number)
        print("ok!")
    else:
        print("quitting...")
        break
