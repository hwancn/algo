# -*- coding: utf-8 -*-
"""
基于单链表实现的链式队列
假设节点数据存储的是字符串
"""

import sys
sys.path.append('../')

from stack.linked_node import Node


class LinkedQueue:

    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, value):
        """
        入队列
        :param value: 节点存储的值
        :return: 无返回值
        """
        new_node = Node(value)
        if self._tail:
            # 非空队列
            self._tail.next_node = new_node
        else:
            # 空队列
            self._head = new_node
        self._tail = new_node

    def dequeue(self):
        if self._head:
            value = self._head.data
            self._head = self._head.next_node
            if self._head is None:
                # 最后一个节点被出队列了
                self._tail = None
            return value

    def __repr__(self):
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current.next_node
        return ' -> '.join(value for value in values)
