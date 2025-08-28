def search(d : dict, name : str):
    if name in d:
        if len(d[name]) == 1:
            return d[name][0]
        else:
            numbers = ""
            list_length = len(d[name])
            for i in range(list_length-1):
                numbers += f"{d[name][i]}\n"
            numbers += f"{d[name][list_length-1]}"
            return numbers
    else:
        return "no number"

def add(d: dict, name : str, number : str):
    if name not in d:
        d[name] = []
    d[name].append(number)
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
