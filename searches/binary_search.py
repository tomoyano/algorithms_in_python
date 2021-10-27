"""二分探索法

探索対象のデータがあらかじめ昇順または降順に並んでいる前提
"""
from typing import List, Optional


def binary_search(search_list: List[int], target: int):
    def __calc_center(head: int, tail: int) -> int:
        return round((head + tail) / 2)

    def __binary_search(search_list: List[int], target: int, head: int, tail: int) -> int:
        # 探索が終了したら None を返す
        if head > tail:
            return

        center: int = __calc_center(head, tail)

        if search_list[center] == target:
            return center
        elif search_list[center] > target:
            return __binary_search(search_list, target, head, center - 1)
        else:
            return __binary_search(search_list, target, center + 1, tail)

    head = 0
    tail = len(search_list) - 1
    return  __binary_search(search_list, target, head, tail)


if __name__ == '__main__':
    search_list = [i for i in range(1, 501, 1)]
    target = 499

    target_index: Optional[int] = binary_search(search_list, target)

    if target_index:
        print(f'target_index: {target_index}')
    else:
        print(f'Target not exist.')
