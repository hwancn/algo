# -*- coding: utf-8 -*-
"""
插入排序以及插入排序的优化版本希尔排序
希尔排序是不稳定的
"""


def insert_sort(ary) -> list:
    """
    :param ary: 列表
    :return: 排序之后的列表
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    for i in range(1, length):
        value = ary[i]
        j = i - 1
        while j >= 0 and ary[j] > value:
            ary[j+1] = ary[j]
            j -= 1
        ary[j+1] = value
    return ary


def shell_sort(ary) -> list:
    """
    希尔排序 可以参考下，https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F
    :param ary: 列表
    :return: 排序之后的列表
    """
    length = len(ary)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            value = ary[i]
            j = i - gap
            while j >= 0 and ary[j] > value:
                ary[j+gap] = ary[j]
                j -= gap
            ary[j+gap] = value
        gap = gap // 2
    return ary


if __name__ == '__main__':
    test_list = [4, 5, 6, 3, 1, 2]
    print(insert_sort(test_list))
    test_list = [4, 5, 6, 3, 1, 2]
    print(shell_sort(test_list))