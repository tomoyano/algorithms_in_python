"""バブルソート(単純交換法)
"""
from typing import List


def bubble_sort(target: List[int]):
    l: int = len(target)
    target_index: int = 0

    for _ in range(l):
        if target_index > l - 2:
            break

        for j in range(l):
            if l - 1 - j == target_index:
                break

            if target[l - 1 - j] < target[l - 2 - j]:
                t: int = target[l - 2 - j]
                target[l - 2 - j] = target[l - 1 - j]
                target[l - 1 - j] = t

        target_index += 1


if __name__ == '__main__':
    lst: List[int] = [5, 3, 4, 1, 2, 5, 3, 1, 8, 10, 7]
    sorted_lst: List[int] = bubble_sort(lst)

    print(lst)
