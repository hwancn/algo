# -*- coding: utf-8 -*-


class Node:
    """链表中的节点"""

    def __init__(self, data, next_node=None):
        """
        :param data: 节点数据
        :param nex_node: 下一个节点的地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """
        :return: 返回节点数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """Node节点存储数据设置方法
        :param data: 新的存储数据
        :return:
        """
        self.__data = data

    @property
    def next_node(self):
        """
        当前节点的下一个节点
        :return: 当前节点的下一个节点的引用
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """
        修改当前节点的下一个节点
        :param next_node: 新的节点引用
        :return:
        """
        self.__next = next_node

    def __repr__(self):
        return 'Node({value})'.format(value=self.data)
