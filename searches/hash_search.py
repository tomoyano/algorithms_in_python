"""ハッシュ探索法
"""
from pprint import pprint
from typing import List, Optional


def calc_hash(x: int, y: int) -> int:
    return x % y


def create_keeper(length: int) -> List[int]:
    return [0 for _ in range(length)]


def add_to_list(keeper: List[int], target: int):
    # ハッシュ値
    hash_value: int = calc_hash(target, len(keeper))

    index: int = hash_value
    for _ in range(len(keeper)):
        if keeper[index] == 0:
            keeper[index] = target
            break

        index = (index + 1) % len(keeper)


def search_by_hash(keeper: List[int], target: int) -> Optional[int]:
    hash_value: int = calc_hash(target, len(keeper))

    index: int = hash_value
    for _ in range(len(keeper)):
        if keeper[index] == target:
            return index

        if keeper[index] == 0:
            # ここに来るということは
            print(f'Target value not exist in list. target: {target}')
            return None

        index = (index + 1) % len(keeper)


if __name__ == '__main__':
    keeper: List[int] = create_keeper(10)
    add_to_list(keeper, 7)
    add_to_list(keeper, 12)
    add_to_list(keeper, 17)
    add_to_list(keeper, 5)
    add_to_list(keeper, 22)
    pprint(keeper)

    index: int = search_by_hash(keeper, 22)
    print(f'index: {index}, value: {keeper[index]}')

    index: int = search_by_hash(keeper, 100)
