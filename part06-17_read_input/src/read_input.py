def read_input(written_number, min_val, max_val):
    while True:
        try:
            user_input = int(input(written_number))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"You must type in an integer between {min_val} and {max_val}")
        except ValueError:
            print(f"You must type in an integer between {min_val} and {max_val}")

