# -*- coding: utf-8 -*-
"""
二分查找的递归形式，
非递归的可以自己实现下
"""

from typing import List


def bsearch(ary: List[int], target: int) -> int:
    """
    假设数组中存储的是整数，其他的类似
    :param ary: 列表
    :param target: 目标元素
    :return: 目标元素在列表中的index, 如果不存在则返回-1
    """
    length = len(ary)
    if length == 0:
        return -1
    return bsearch_internally(ary, 0, length - 1, target)


def bsearch_internally(ary: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1
    mid = low + ((high - low) >> 1)
    if ary[mid] == target:
        return mid
    elif ary[mid] > target:
        return bsearch_internally(ary, low, mid-1, target)
    else:
        return bsearch_internally(ary, mid+1, high, target)


if __name__ == '__main__':
    test_list = [1, 3, 5, 7, 9, 10]
    target = 3
    print(bsearch(test_list, target))
