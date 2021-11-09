"""単純選択法
"""
from typing import List


def selection_sort(lst: List[int]):
    for i in range(len(lst)):
        min_index: int = i

        # リストの最後の要素についてはすでに最大値が入っているためブレイク
        # 下のfor文は実行されないためこのブレイクはいらないが、参考書に倣ってブレイクしている
        if i == len(lst) - 1:
            break

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        swap_num: int = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = swap_num


if __name__ == '__main__':
    lst: List[int] = [5, 2, 1, 4, 3, 1, 4]
    selection_sort(lst)
    print(lst)
