# -*- coding: utf-8 -*-
"""
归并排序
"""

from typing import List


def merge_sort(ary: List[int]):
    """
    归并排序，假设元素是整数，其他类似
    :param ary: 列表
    :return:
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    merge_sort_between(ary, 0, length-1)


def merge_sort_between(ary: List[int], low: int, high: int):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort_between(ary, low, mid)
        merge_sort_between(ary, mid+1, high)
        merge(ary, low, mid, high)


def merge(ary: List[int], low: int, mid: int, high: int):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j <= high:
        if ary[i] <= ary[j]:
            tmp.append(ary[i])
            i += 1
        else:
            tmp.append(ary[j])
            j += 1
    if i > mid:
        # 前半部分全部完成，将后半部分全部加入
        tmp.extend(ary[j:high+1])
    else:
        # 后半部分全部完成，将前半部分全部加入
        tmp.extend(ary[i:mid+1])
    ary[low:high+1] = tmp


if __name__ == '__main__':
    test_list = [4, 5, 6, 3, 1, 2]
    merge_sort(test_list)
    print(test_list)
