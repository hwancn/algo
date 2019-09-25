# -*- coding: utf-8 -*-
"""
字符串匹配算法
"""
from time import time


def bf(main: str, pattern: str) -> int:
    """
    朴素字符串匹配算法，时间复杂度是O(n*m)
    :param main: 主串
    :param pattern: 模式串
    :return: 主串中的下标，没有的话返回-1
    """
    n = len(main)
    m = len(pattern)

    if n < m:
        return -1
    if n == m and main == pattern:
        return 0
    for i in range(n-m+1):
        for j in range(m):
            if main[i+j] == pattern[j]:
                if j == m-1:
                    # 全部相等
                    return i
                else:
                    continue
            else:
                break
    return -1


def rk(main: str, pattern: str) -> int:
    """
    bk字符串匹配算法，时间复杂度是O(n)
    :param main: 主串
    :param pattern: 模式串
    :return: 主串中的下标，没有的话返回-1
    """
    n = len(main)
    m = len(pattern)

    if n < m:
        return -1
    if n == m and main == pattern:
        return 0

    # 为了配合下面的hash算法，避免重复计算，先计算出26的m-1次方的值
    # 假设字符串里面只有a-z这26个小写字母
    cal_list = [None] * m
    for i in range(m):
        cal_list[i] = 26 ** i

    def simple_hash(s):
        """
        计算hash值， s的长度为m
        """
        ret = 0
        ord_a = ord('a')
        for index, sub_s in enumerate(s):
            ret += (ord(sub_s) - ord_a) * cal_list[m-1-index]
        return ret

    # 计算模式串的hash值
    hash_pattern = simple_hash(pattern)
    # 计算主串的hash值表
    hash_main = [None] * (n-m+1)
    hash_main[0] = simple_hash(main[0:m])
    for i in range(1, n-m+1):
        hash_main[i] = (hash_main[i-1] - cal_list[m-1] * (ord(main[i-1]) - ord('a'))) * 26 + (ord(main[i+m-1]) - ord('a'))
    for i, h in enumerate(hash_main):
        if h == hash_pattern:
            return i
        else:
            continue
    return -1


if __name__ == '__main__':
    m_str = 'a'*10000
    p_str = 'a'*200+'b'

    print('--- time consume ---')
    t = time()
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time()-t))

    t = time()
    print('[rk] result:', rk(m_str, p_str))
    print('[rk] time cost: {0:.5}s'.format(time()-t))

    print('')
    print('--- search ---')
    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'jump'
    print('[bf] result:', bf(m_str, p_str))
    print('[rk] result:', rk(m_str, p_str))

"""
--- time consume ---
[bf] result: -1
[bf] time cost: 0.28831s
[rk] result: -1
[rk] time cost: 0.007596s

--- search ---
[bf] result: 16
[rk] result: 16
"""
