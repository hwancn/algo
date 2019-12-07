# -*- coding: utf-8 -*-
# 求平方根
# 原题：https://leetcode-cn.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        target = x
        left, right = 1, x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid > target:
                right = mid - 1
            else:
                left = mid
        return left
