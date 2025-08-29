from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    selection = sample(list(range(lower, upper + 1)), amount)
    selection.sort()
    return selection
