# -*- coding: utf-8 -*-
"""
bm算法，可以参考：https://time.geekbang.org/column/article/71525
假设我们需要匹配的都是ascii码
"""

SIZE = 256


def generate_bc(pattern, m, bc):
    """
    生成坏字符串hash表
    :param pattern: 模式串
    :param m: 模式串长度
    :param bc: hash表
    :return:
    """
    for i in range(m):
        # 后面的会覆盖前面的
        bc[ord(pattern[i])] = i


def generate_gs(pattern, m, suffix, prefix):
    """
    好后缀预处理
    :param pattern: 模式串
    :param m: 模式串长度
    :param suffix: suffix数组
    :param prefix: prefix数组
    :return:
    """
    for i in range(m-1):
        k = 0   # 公共后缀子串长度
        for j in range(i, -1, -1):
            if pattern[j] == pattern[m-1-k]:  # 与pattern[0, m-1]求公共后缀子串
                k += 1
                suffix[k] = j
                if j == 0:
                    prefix[k] = True
            else:
                break


def move_by_gs(j, m, suffix, prefix):
    """
    通过好后缀计算移动值，
    需要处理三种情况：
    1. 整个好后缀在pattern中可以找到
    2. 如果第一个不满足，查看好后缀子串是否可以在pattern的前缀匹配
    3.如果前两个都不满足的话，直接移动m个位置
    :param j: 表示坏字符对应的模式串中的字符的下标
    :param m: 模式串的长度
    :param suffix: suffix数组
    :param prefix: prefix数组
    :return: 应该移动的位数
    """
    k = m - 1 - j  # 好后缀长度
    if suffix[k] != -1:
        # 整个好后缀在模式串pattern中有出现
        return j - suffix[k] + 1
    else:
        for r in range(j+2, m):
            # 判断好后缀的子串是否和模式串pattern的前缀相匹配
            if prefix[m-r]:
                return r
        return m


def bm(main, pattern):
    """
    bm字符串匹配算法
    :param main: 主串
    :param pattern: 模式串
    :return: 匹配的主串的其实位置，不匹配则返回-1
    """
    n = len(main)
    m = len(pattern)

    if n < m:
        return -1
    if n == m and main == pattern:
        return 0

    # bc
    bc = [-1] * SIZE
    generate_bc(pattern, m, bc)

    # gs
    suffix = [-1] * m
    prefix = [False] * m
    generate_gs(pattern, m, suffix, prefix)

    i = 0
    while i < (n-m+1):
        j = m - 1
        # 从后面向前面比较
        while j >= 0:
            if main[i+j] == pattern[j]:
                j -= 1
            else:
                break
        if j == -1:
            # 完全匹配
            return i
        # 根据坏字符串规则计算后移位数
        x = j - bc[ord(main[i+j])]

        # 根据好后缀规则计算后移位数
        y = 0
        # 先判断下是否存在好后缀
        if j != (m-1):
            # 存在后缀
            y = move_by_gs(j, m, suffix, prefix)
        # 移动位数从坏字符串和好后缀中取大的
        i += max(x, y)
    return -1


if __name__ == '__main__':
    print('--- search ---')
    m_str = 'dfasdeeeetewtweyyyhtruuueyytewtweyyhtrhrth'
    p_str = 'eyytewtweyy'
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[bm] result:', bm(m_str, p_str))