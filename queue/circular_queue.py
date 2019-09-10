# -*- coding: utf-8 -*-
"""
循环队列，
循环队列必须要有个容量，所以理想对应数组实现的队列
关于为什么'循环队列'需要浪费一个空间的思考，个人觉得更多的是区别开空队列和满队列的判断条件，
当然也可以不浪费一个空间，比如多加一个字段，保存队列中的元素个数，然后和容量capacity比较
本示例是最普通的实现，假设存储的数据为字符串
"""

from itertools import chain


class CircularQueue:

    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value: str) -> bool:
        """
        入队列
        :param value: 存储的值
        :return: True 表示入队列成功， False表示失败
        """
        # 判断是否满队列
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._items.append(value)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> str:
        """
        出队列
        :return: 出队列值
        """
        # 判断是否为空队列
        if self._head == self._tail:
            return None
        value = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return value

    def __repr__(self):
        if self._tail >= self._head:
            return ' '.join(item for item in self._items[self._head: self._tail])
        else:
            return ' '.join(item for item in chain(self._items[self._head], self._items[:self._tail]))
