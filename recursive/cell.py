# -*- coding: utf-8 -*-
# 细胞分裂问题
"""
细胞分裂 有一个细胞 每一个小时分裂一次，一次分裂一个子细胞，第三个小时后会死亡。那么n个小时候有多少细胞？试着分析下这个递归算法的时间复杂度是多少呢
"""

# 思路分析
# 第一个小时，只有a态细胞；第二个小时，a态细胞分裂，原来的a态细胞变成了b态细胞，分裂出来的细胞变成了新的a态细胞；第三个小时，a态细胞继续分裂变成b态细胞和新的a态细胞，b态细胞分裂变成c态细胞和a态细胞；第四个小时，a、b、c态细胞都会分裂，并且按照之前的规律转变。得出下面的结论
# a 初始态 一个小时 前一个小时的 a+b+c
# b 幼年态 两个小时 前一个小时的 a
# c 成熟态 三个小时 前一个小时的 b

# 假设第一个小时的时候细胞个数为1，即f(1) = 1
# 并且为了问题的简便，假设是细胞先分裂再死亡


def all_cell(n: int) -> int:
    # a态细胞
    def a_cell(n: int) -> int:
        if n == 1:
            return 1
        else:
            return a_cell(n-1) + b_cell(n-1) + c_cell(n-1)

    def b_cell(n: int) -> int:
        if n == 1:
            return 0
        else:
            return a_cell(n-1)

    def c_cell(n: int) -> int:
        if n == 1 or n == 2:
            return 0
        else:
            return b_cell(n-1)

    if n < 1:
        # n 必须大于等于1
        return 0
    else:
        return a_cell(n) + b_cell(n) + c_cell(n)


def all_cell2(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 7
    else:
        return 2 * all_cell2(n-1) - all_cell2(n-4)


if __name__ == '__main__':
    for i in range(1, 11):
        print('第{n}个小时， 细胞个数是{cell_num}'.format(n=i, cell_num=all_cell(i)))
        print('第{n}个小时， 细胞个数是{cell_num}'.format(n=i, cell_num=all_cell2(i)))
        print('----' * 40)
