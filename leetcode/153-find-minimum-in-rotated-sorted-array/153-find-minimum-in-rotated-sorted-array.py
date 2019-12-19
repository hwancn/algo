# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return -1
        i, j = 0, length-1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] < nums[j]:
                # 右边有序
                j = mid
            else:
                # 右边无序
                i = mid + 1
        return nums[i]
