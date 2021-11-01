"""ハッシュ探索法
"""
from pprint import pprint
from typing import List


def create_keeper(length: int) -> List[int]:
    return [0 for _ in range(length)]

def add_to_list(keeper: List[int], target:int):
    # ハッシュ値
    hash_value: int = target % len(keeper)

    index: int = hash_value
    for _ in range(len(keeper)):
        if keeper[index] == 0:
            keeper[index] = target
            break
        
        index = (index + 1) % len(keeper)


if __name__ == '__main__':
    keeper: List[int] = create_keeper(5)
    add_to_list(keeper, 7)
    add_to_list(keeper, 12)
    add_to_list(keeper, 17)
    add_to_list(keeper, 5)
    add_to_list(keeper, 22)
    pprint(keeper)
