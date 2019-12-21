# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        length = len(nums)
        l, r = 1, length-1
        while l < r:
            l_count = 0
            mid = l + (r - l + 1) // 2
            for num in nums:
                if num < mid:
                    l_count += 1
            if l_count < mid:
                l = mid
            else:
                r = mid - 1
        return l
