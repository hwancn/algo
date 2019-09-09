# -*- coding: utf-8 -*-
# 基于链表实现的栈

import sys
sys.path.append('../')

from stack.linked_node import Node


class LinkedStack:
    """
    基于单链表实现的栈
    """
    def __init__(self):
        self.__top: Node = None

    @property
    def top(self) -> Node:
        """
        栈顶元素
        :return:
        """
        return self.__top

    def empty(self):
        """
        清空栈
        :return: 无返回值
        """
        self.__top = None

    def is_empty(self) -> bool:
        """
        是否为空栈
        :return:  True or False
        """
        return not self.__top

    def push(self, value):
        """
        压入栈
        :param value: 节点存储的数据
        :return:
        """
        new_node = Node(value)
        new_node.next_node = self.__top
        self.__top = new_node

    def pop(self):
        """
        弹出栈
        :return: 弹出节点保存的数据
        """
        if self.__top is None:
            return
        value = self.__top.data
        self.__top = self.__top.next_node
        return value

    def __repr__(self) -> str:
        current = self.__top
        items = []
        while current:
            items.append(current)
            current = current.next_node
        return ' '.join(str(item) for item in items)


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
