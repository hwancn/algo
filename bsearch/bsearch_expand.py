# -*- coding: utf-8 -*-
"""
二分查找的变形
主要为一下四种情况
- 查找第一个等于给定值的元素
- 查找最后一个等于给定值的元素
- 查找第一个大于等于给定值的元素
- 查找最后一个小于等于给定值的元素

假设数组中存储的是整数，其他的类似
"""

from typing import List


def bsearch_1(ary: List[int], target: int) -> int:
    """
    查找第一个等于给定值的元素
    :param ary: 列表
    :param target: 目标元素
    :return: 所求在列表中的index, 如果不存在则返回-1
    """
    length = len(ary)
    if length == 0:
        return -1
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if ary[mid] > target:
            high = mid - 1
        elif ary[mid] < target:
            low = mid + 1
        else:
            if mid == 0 or ary[mid-1] != target:
                return mid
            else:
                high = mid - 1
    return -1


def bsearch_2(ary: List[int], target: int) -> int:
    """
    查找最后一个等于给定值的元素
    :param ary: 列表
    :param target: 目标元素
    :return: 所求在列表中的index, 如果不存在则返回-1
    """
    length = len(ary)
    if length == 0:
        return -1
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if ary[mid] > target:
            high = mid - 1
        elif ary[mid] < target:
            low = mid + 1
        else:
            if mid == length-1 or ary[mid+1] != target:
                return mid
            else:
                low = mid + 1
    return -1


def bsearch_3(ary: List[int], target: int) -> int:
    """
    查找第一个大于等于给定值的元素
    :param ary: 列表
    :param target: 目标元素
    :return: 所求在列表中的index, 如果不存在则返回-1
    """
    length = len(ary)
    if length == 0:
        return -1
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if ary[mid] >= target:
            if mid == 0 or ary[mid-1] < target:
                return mid
            else:
                high = mid - 1
        elif ary[mid] < target:
            low = mid + 1
    return -1


def bsearch_4(ary: List[int], target: int) -> int:
    """
    查找最后一个小于等于给定值的元素
    :param ary: 列表
    :param target: 目标元素
    :return: 所求在列表中的index, 如果不存在则返回-1
    """
    length = len(ary)
    if length == 0:
        return -1
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if ary[mid] > target:
            high = mid - 1
        elif ary[mid] <= target:
            if mid == length-1 or ary[mid+1] > target:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == "__main__":
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22, 22]
    print(len(a))

    print(bsearch_1(a, 0) == -1)
    print(bsearch_1(a, 1) == 0)
    print(bsearch_1(a, 22) == 11)
    print(bsearch_1(a, 7) == 6)
    print(bsearch_1(a, 30) == -1)

    print(bsearch_2(a, 0) == -1)
    print(bsearch_2(a, 1) == 1)
    print(bsearch_2(a, 22) == 12)
    print(bsearch_2(a, 7) == 9)
    print(bsearch_2(a, 30) == -1)

    print(bsearch_3(a, 0) == 0)
    print(bsearch_3(a, 1) == 0)
    print(bsearch_3(a, 5) == 5)
    print(bsearch_3(a, 7) == 6)
    print(bsearch_3(a, 22) == 11)
    print(bsearch_3(a, 30) == -1)

    print(bsearch_4(a, 0) == -1)
    print(bsearch_4(a, 1) == 1)
    print(bsearch_4(a, 6) == 5)
    print(bsearch_4(a, 7) == 9)
    print(bsearch_4(a, 7) == 9)
    print(bsearch_4(a, 22) == 12)
    print(bsearch_4(a, 30) == 12)

    # 打印全部为True
