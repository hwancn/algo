# -*- coding: utf-8 -*-
"""
我们假设堆的数据是从数组下标0开始存储的
"""


class BinaryHeap:
    """
    大顶推
    """
    def __init__(self, data: list):
        """
        :param data: 数据， 列表
        """
        self._data = data

    def heapify(self):
        """
        构建大顶堆, 时间复杂度是O(n),不是O(nlogn),参见 https://time.geekbang.org/column/article/69913
        """
        n = len(self._data)
        first = n // 2 - 1   # 最后一个非叶子节点下标
        for start in range(first, -1, -1):  # 构建最大堆
            self._heapify(self._data, start, n-1)

    def _heapify(self, ary, start, end):
        """
        自上而下的调整堆
        最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
        start为当前需要调整最大堆的位置，end为调整边界
        """
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            # 判断右节点是否存在, 并且判断右节点是否大于左节点
            if child + 1 <= end and ary[child] < ary[child+1]:
                child = child + 1
            if ary[root] < ary[child]:
                # 父节点小于左右节点中较大的那个
                # 交换
                ary[root], ary[child] = ary[child], ary[root]
                # 继续向下
                root = child
            else:
                # 不需要交换，直接退出循环
                break

    def heappop(self):
        """
        弹出堆顶的最值，时间复杂度是O(logn)
        :return:
        """
        n = len(self._data)
        if n == 0:
            # 堆中没有元素
            return None
        heap_root = self._data[0]
        self._data[0] = self._data[n-1]
        self._data.pop() # 在将最后一个元素置为堆顶之后，将其弹出
        self._heapify(self._data, 0, n-2)  # end此处为n-2，弹出了一个元素
        return heap_root

    def heappush(self, val):
        """
        不考虑堆满的情况
        向堆里面添加一个元素，O(logn)
        添加到尾部，然后自下而上调整堆
        :param val:
        :return:
        """
        self._data.append(val)
        i = len(self._data) - 1
        # 当前节点是i，子节点的下标是(i-1)//2
        while (i-1)//2 > 0 and self._data[i] > self._data[(i-1)//2]:
            self._data[i], self._data[(i-1)//2] = self._data[(i-1)//2], self._data[i]
            i = (i-1) // 2

    def heap_sort(self):
        """
        堆排序
        """
        # 先构建最大堆
        self.heapify()
        n = len(self._data)
        for end in range(n-1, 0, -1):
            self._data[end], self._data[0] = self._data[0], self._data[end]
            self._heapify(self._data, 0, end-1)

    def __repr__(self):
        vals = [str(i) for i in self._data]
        return '>'.join(vals)


if __name__ == '__main__':
    h = BinaryHeap([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    h.heapify()
    print('1: ', h)
    print('2: ', h.heappop())
    print('3: ', h)
    h.heappush(3.5)
    print('4: ', h)
    h.heappush(0.1)
    print('5: ', h)
    h.heappush(0.5)
    print('6: ', h)
    print('7: ', h.heappop())
    print('8: ', h)
    h.heap_sort()
    print('9: ', h)

'''
1:  11>10>6>8>9>5>0>7>3>1>4>2
2:  11
3:  10>9>6>8>4>5>0>7>3>1>2
4:  10>9>6>8>4>5>0>7>3>1>2>3.5
5:  10>9>6>8>4>5>0>7>3>1>2>3.5>0.1
6:  10>9>6>8>4>5>0.5>7>3>1>2>3.5>0.1>0
7:  10
8:  9>8>6>7>4>5>0.5>0>3>1>2>3.5>0.1
9:  0>0.1>0.5>1>2>3>3.5>4>5>6>7>8>9

'''
