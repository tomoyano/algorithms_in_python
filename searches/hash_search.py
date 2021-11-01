"""ハッシュ探索法
"""
from typing import List


def create_keeper(length: int) -> List[int]:
    return [0 for _ in range(length)]

def add_to_list(keeper: List[int], target:int):
    # ハッシュ値
    hash_value: int = target % length

    index: int = hash_value
    while True:
        if keeper[index] == 0:
            keeper[index] == target
            break
        
        index = (index + 1) % len(keeper)
