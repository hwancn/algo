# -*- coding: utf-8 -*-
"""
冒泡排序和两个优化版本
默认从小到大排序
"""


def bubble_sort(ary) -> list:
    """
    :param ary: 列表
    :return: 返回列表
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    for i in range(length):
        for j in range(1, length-i):
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
    return ary


def bubble_sort2(ary) -> list:
    """
    冒泡排序优化点，如果某次冒泡，没有发生交换，表明此时已经全部排好序了，后面的冒泡都不需要进行了
    :param ary: 列表
    :return: 返回列表
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    for i in range(length):
        made_swap = False
        for j in range(1, length-i):
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
                made_swap = True
        if not made_swap:
            break
    return ary


def bubble_sort3(ary) -> list:
    """
    冒泡排序优化点，如果某次冒泡，没有发生交换，表明此时已经全部排好序了，后面的冒泡都不需要进行了
    此外，还可以记录上一次交换的位置，因为这个位置之后的数据都是已经排好序的了，下一次冒泡的时候不需要对这之后的数据进行再次排序
    :param ary: 列表
    :return: 返回列表
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    k = length
    for i in range(length):
        made_swap = False
        for j in range(1, k):
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
                made_swap = True
                k = j
        if not made_swap:
            break
    return ary


if __name__ == '__main__':
    test_list = [4, 5, 6, 3, 1, 2]
    print(bubble_sort(test_list))
    test_list = [4, 5, 6, 3, 1, 2]
    print(bubble_sort2(test_list))
    test_list = [4, 5, 6, 3, 1, 2]
    print(bubble_sort3(test_list))