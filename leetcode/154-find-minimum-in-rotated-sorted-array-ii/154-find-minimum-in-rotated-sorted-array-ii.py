# -*- coding: utf-8 -*-
# 解题思路： https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/154-find-minimum-in-rotated-sorted-array-ii-by-jyd/

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
            elif nums[mid] > nums[j]:
                # 右边无序，最小值存在于右边
                i = mid + 1
            else:
                j = j - 1
        return nums[i]