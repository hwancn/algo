# -*- coding: utf-8 -*-
"""
可能deeps不好理解，下面举例子来理解下
比如
第二级索引 1---------->7----------->13
第一级索引 1---->4---->7---->9----->13
原始链表  1->3->4->5->7->8->9->10->13

这个例子里面，对于1这个SkipListNode(1)的deeps为[SkipListNode(3), SkipListNode(4), SkipListNode(7)],
           对于4这个SkipListNode(4)的deeps为[SkipListNode(5), SkipListNode(7)]
"""

import random


class SkipListNode(object):
    def __init__(self, val, high=1):
        # 节点存储的值
        self.data = val
        # 节点对应索引层的深度
        self.deeps = [None] * high


class SkipList(object):
    """
        An implementation of skip list.
        The list stores positive integers without duplicates.
        跳表的一种实现方法。
        跳表中储存的是正整数，并且储存的是不重复的。
        Author: Ben
    """

    def __init__(self):
        # 索引层的最大深度
        self.__MAX_LEVEL = 16
        # 跳表的高度
        self._high = 1
        # 每一索引层的首节点, 默认值为None
        self._head = SkipListNode(None, self.__MAX_LEVEL)

    def find(self, val):
        cur = self._head
        # 从索引层的顶层，逐层定位到要查找的值
        # 索引层上下是对应的，下层的起点是上一个索引层中小于插入值的最大值对于的起点
        for i in range(self._high-1, -1, -1):
            # 在同一索引层内，找到小于目标值的最大的节点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
        # 如果存在的话，此时的cur是目标节点的前一个节点
        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self, val):
        """
        新增时, 通过随机函数获取要更新的索引层数,
        要对低于给定高度的索引层添加新结点的指针
        """
        high = self.randomLevel()
        if self._high < high:
            self._high = high
        # 申请新节点
        newNode = SkipListNode(val, high)
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * high
        cur = self._head

        for i in range(high-1, -1, -1):
            # 每个索引层内寻找小于插入值的节点
            # 索引层上下是对应的，下层的起点是上一个索引层中小于插入值的最大值对于的起点
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        # 在小于高度的每个索引层插入新节点
        for i in range(high):
            # 类似这种 new.next = prev.next \ prev.next = new.next
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode

    def delete(self, val):
        '''
        删除时, 要将每个索引层中对应的节点都删掉
        '''
        # cache用来缓存对应索引层中小于插入值的最大节点
        cache = [None] * self._high
        cur = self._head
        # 缓存每一个索引层定位小于插入值的节点
        for i in range(self._high - 1, -1, -1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur
        # 如果给定的值存在, 更新索引层中对应的节点
        # 此时的cur是小于目标值的最大的那个节点了
        if cur.deeps[0] and cur.deeps[0].data == val:
            # 目标值存在，需要删除其他层的索引
            for i in range(self._high-1, -1, -1):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLevel(self, p=0.5):
        '''
           理论来讲，一级索引中元素个数应该占原始数据的 50%，二级索引中元素个数占 25%，三级索引12.5% ，一直到最顶层。
           因为这里每一层的晋升概率是 50%。对于每一个新插入的节点，都需要调用 randomLevel 生成一个合理的层数。
           该 randomLevel 方法会随机生成 1~MAX_LEVEL 之间的数，且 ：
                  50%的概率返回 1
                  25%的概率返回 2
                12.5%的概率返回 3 ...
        '''
        high = 1
        while random.random() < p and high < self.__MAX_LEVEL:
            high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)


if __name__ == '__main__':
    sl = SkipList()
    for i in range(100):
        sl.insert(i)
    p = sl.find(7)
    print(p.data)
    sl.delete(37)
    print(sl)
    sl.delete(37.5)
    print(sl)