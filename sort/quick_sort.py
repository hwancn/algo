# -*- coding: utf-8 -*-
"""
快速排序
"""


def quick_sort_two_ways(ary) -> list:
    """
    快速排序，两边指针遍历然后交换
    :param ary: 列表
    :return: 列表
    """

    def quick_sort(ary, left: int, right: int) -> list:
        if left >= right:
            return ary
        # 取左边的为基准数
        key = ary[left]
        lp = left
        rp = right
        while lp < rp:
            while ary[rp] >= key and lp < rp:
                rp -= 1
            while ary[lp] <= key and lp < rp:
                lp += 1
            ary[lp], ary[rp] = ary[rp], ary[lp]
        ary[left], ary[rp] = ary[rp], ary[left]
        quick_sort(ary, left, rp-1)
        quick_sort(ary, rp+1, right)
        return ary
    length = len(ary)
    if length == 0 or length == 1:
        return ary
    return quick_sort(ary, 0, length-1)


if __name__ == '__main__':
    test_list = [4, 5, 6, 3, 1, 2]
    print(quick_sort_two_ways(test_list))