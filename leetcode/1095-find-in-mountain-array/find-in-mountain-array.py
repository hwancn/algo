# -*- coding: utf-8 -*-

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.size


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        mountaintop = self._find_mountaintop(mountain_arr, 0, size - 1)
        res = self._find_from_sorted_arr(mountain_arr, 0, mountaintop, target)
        if res != -1:
            return res
        return self._find_from_inversed_arr(mountain_arr, mountaintop+1, size-1, target)

    def _find_mountaintop(self, mountain_arr: 'MountainArray', l: int, r: int):
        # 找到山脉数组的最大值
        while l < r:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                # 升序
                l = mid + 1
            else:
                r = mid
        return l

    def _find_from_sorted_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在前半部分升序数组中中寻找target
        while l < r:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        else:
            return -1

    def _find_from_inversed_arr(self, mountain_arr: 'MountainArray', l: int, r: int, target: int):
        # 在后半部分降序数组中查找
        while l < r:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        else:
            return -1

