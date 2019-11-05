# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
有序旋转数组的二分查找
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        length = len(nums)
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[end]:
                # 右边有序
                if nums[mid] < target <= nums[end]:
                    # target 在右边
                    start = mid + 1
                else:
                    # target 在左边
                    end = mid - 1
            else:
                # 左边有序
                if nums[start] <= target < nums[mid]:
                    # target在左边有序里面
                    end = mid - 1
                else:
                    # target 在右边
                    start = mid + 1
        return -1





