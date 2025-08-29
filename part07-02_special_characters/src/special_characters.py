from string import *

def separate_characters(my_string: str):
    letters = ''.join([c for c in my_string if c in ascii_letters])
    punct_characters = ''.join([c for c in my_string if c in punctuation])
    others = ''.join([c for c in my_string if c not in ascii_letters and c not in punctuation])
    return (letters, punct_characters, others)

