# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/palindrome-number/
回文数的判断，需要考虑大值溢出

分别取高位和低位来判断
例如：
95349 % 1000 => 95349 % 10^4 = 5349
95349 // 10 = 9534
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a, h = x, 1
        while a // h >= 10:
            h = h * 10

        while a > 0:
            if a // h != a % 10:
                return False
            a = a % h   # 去掉头
            a = a // 10  # 去掉尾
            h = h // 100
        return True
