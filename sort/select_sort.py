# -*- coding: utf-8 -*-
"""
选择排序
"""


def select_sort(ary) -> list:
    """
    :param ary: 列表
    :return: 排序之后的列表
    """
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    for i in range(length):
        min_value = ary[i]
        min_index = i
        for j in range(i+1, length):
            if ary[j] < min_value:
                min_index = j
                min_value = ary[j]
        # 交换
        ary[min_index], ary[i] = ary[i], ary[min_index]
    return ary


if __name__ == '__main__':
    test_list = [4, 5, 6, 3, 1, 2]
    print(select_sort(test_list))