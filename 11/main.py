from pprint import pprint
from copy import deepcopy
from typing import List

# stone_list = [125, 17]
stone_list = [7725,185,2,132869,0,1840437,62,26310]
blinks = 25
current_blink = 1
next_stone_list = []

def transform(stone: int) -> List[int]:
    stone_str = str(stone)
    str_len = len(stone_str)
    if stone == 0:
        return [1]
    if str_len % 2 == 0:
        left = int(stone_str[:(str_len // 2)])
        right = int(stone_str[-(str_len // 2):])
        return [left, right]
    else:
        return [stone * 2024]

while current_blink <= blinks:
    next_stone_list = []
    for stone in stone_list:
        next_stone_list.extend(transform(stone))

    stone_list = next_stone_list
    current_blink += 1

print(len(stone_list))