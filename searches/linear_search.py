"""線形探索

探索のターゲットを先頭から順に調べていく方法。
単純でわかりやすいが効率は良くない。
"""
from typing import List, Optional

def linear_search(search_list: List[int], target: int) -> Optional[int]:
    """線形探索

    与えられた整数の配列の中から、ターゲットの数が入っている
    インデックスの番号を返す。

    Args:
        search_list: 探索を行う整数の配列
        target: 探すべき整数
    
    Returns:
        ターゲットの整数があればインデックスの番号
    """
    for i, num in enumerate(search_list):
        if num == target:
            return i
    
    return None  # ターゲットがない場合は None を返すことを明示しておく


if __name__ == '__main__':
    search_list: List[int] = [5, 2, 3, 1, 4, 6, 9, 8, 7, 10, 11]
    target: int = 7

    index: Optional[int] = linear_search(search_list, target)

    if index:
        print(f'target: {target}, index: {index}, num_in_list: {search_list[index]}')
