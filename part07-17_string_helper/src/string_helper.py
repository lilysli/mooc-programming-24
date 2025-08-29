def change_case(orig_string: str) -> str:
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple[str, str]:
    middle = len(orig_string) // 2
    return orig_string[:middle], orig_string[middle:]

def remove_special_characters(orig_string: str) -> str:
    return ''.join(char for char in orig_string if char.isalnum() or char.isspace())