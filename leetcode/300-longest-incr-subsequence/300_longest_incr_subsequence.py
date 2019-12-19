# -*- coding: utf-8 -*-
# 最长递增子序列长度
# 原题： https://leetcode-cn.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        length = len(nums)
        tails, res = [0] * length, 0
        for k in range(length):
            i, j = 0, res
            while i < j:
                m = i + (j - i) // 2  # 取左中位数
                if tails[m] < nums[k]:
                    i = m + 1
                else:
                    j = m
            tails[i] = nums[k]
            if j == res:
                res += 1
        return res


if __name__ == '__main__':
    res = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    print(res)