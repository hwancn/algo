# -*- coding: utf-8 -*-
# 单链表的一些常见操作


class Node:
    """链表中的节点"""

    def __init__(self, data, nex_node=None):
        """
        :param data: 节点数据
        :param nex_node: 下一个节点的地址
        """
        self.__data = data
        self.__next = nex_node

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


class SinglyLinkedList(object):
    """单向列表"""

    def __init__(self):
        """单向列表初始化方法"""
        self.__head = None

    def insert_to_head(self, value):
        """
        在链表的头部插入一个节点
        :param value: 将要存储的数据
        :return: 无返回值(也可以返回链表头)
        """
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_to_tail(self, value):
        """
        在链表尾部插入节点
        :param value: 将要保存的数据
        :return: 无返回值(也可以返回链表头)
        """
        new_node = Node(value)
        node = self.__head
        if node is None:
            # 空链表
            self.__head = new_node
            return
        while node.next_node is not None:
            # 查找尾部节点
            node = node.next_node
        node.next_node = new_node

    def insert_after(self, node: Node, value):
        """
        在某个指定的节点后面插入存储为value的节点
        :param node: 指定节点
        :param value: 存储的值
        :return: 无返回值
        """
        if node is None or self.__head is None:
            # 在空节点后面插入无意义，直接返回
            # 空列表也直接返回
            return
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node: Node, value):
        """
        在指定节点之前插入存储为value的节点
        :param node: 指定节点
        :param value: 存储的值
        :return: 无返回值
        """
        if node is None or self.__head is None:
            return
        if node == self.__head:
            # 表头插入
            self.insert_to_head(value)
        new_node = Node(value)
        pre = self.__head
        not_found = False
        while pre.next_node != node:
            if pre.next_node is None:
                # 到链表尾部了，不存在指定节点
                not_found = True
                break
            else:
                pre = pre.next_node
        if not not_found:
            # pre节点就是指定节点的前一节点
            new_node.next_node = pre.next_node
            pre.next_node = new_node

    def delete_by_node(self, node: Node):
        """
        在链表中删除指定节点
        :param node: 指定节点
        :return: 无返回值
        """
        if self.__head is None or node is None:
            return
        if self.__head == node:
            # 需要删除的指定节点是头结点
            self.__head = self.__head.next_node
            return
        pre = self.__head
        not_found = False  # 标记是否找到指定节点，如果不存在则置为True
        while pre.next_node != node:
            if pre.next_node is None:
                # 指定节点不存在
                not_found = True
                break
            else:
                pre = pre.next_node
        if not not_found:
            pre.next_node = node.next_node
            # or pre.next_node = pre.next_node.next_node

    def delete_by_value(self, value):
        """
        删除指定存储值为value的节点，此方法是删除第一个
        :param value: 指定的值
        :return: 无返回值
        """
        if self.__head is None:
            return
        if self.__head.data == value:
            self.__head = self.__head.next_node
            return
        pre = self.__head
        node = self.__head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:
                # 最后一个节点了
                not_found = True
                break
            else:
                pre = node
                node = pre.next_node
        if not not_found:
            pre.next_node = node.next_node

    def delete_last_n_node(self, n: int):
        """
        删除倒数第n个节点
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        :param n: 指定的系数n
        :return:
        """
        if self.__head is None or n <= 0:
            return

        fast = self.__head
        slow = self.__head
        step = 0

        while (step < n-1) and fast is not None:
            fast = fast.next_node
            step += 1

        if step < n - 1:
            # 边界值，需要自己演示一下
            # 链表长度小于n
            return
        while fast.next_node is not None:
            temp = slow
            fast = fast.next_node
            slow = slow.next_node
        if slow == self.__head:
            # 上面的循环一次都没有执行，在循环外fast已经是最后一个节点，此时slow是头部节点
            # 此时相当于是删除头部节点
            self.__head = self.__head.next_node
            return
        temp.next_node = slow.next_node

    def find_mid_node(self) -> Node:
        """
        找到链表中间的节点
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
            链表的长度为n,如果n为奇数的话，返回中间的那个，如果n为偶数，返回中间前面那个，比如n为4，返回第二个
        :return: Node
        """
        if self.__head is None:
            # 空链表
            return
        fast = self.__head
        slow = self.__head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            if fast is None:
                break
            slow = slow.next_node
        return slow

    def __str__(self):
        pos = self.__head
        if pos is None:
            return '空链表'
        result_list = []
        while pos is not None:
            result_list.append(pos.data)
            pos = pos.next_node
        return ' --> '.join(result_list)

    def find_by_value(self, value) -> Node:
        """
        按照数据值查找单向列表中节点
        :param value: 数据值
        :return: Node
        """
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index) -> Node:
        """
        按照索引查找节点, 第一个节点的index为0
        :param index:
        :return: Node
        """
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    def reversed_self(self):
        """
        翻转链表, 最后通过这个类对象的__head获取
        """
        if self.__head is None or self.__head.next_node is None:
            # 空链表或者只有一个节点的链表
            return
        pre = self.__head
        node = self.__head.next_node
        while node is not None:
            tmp = node.next_node
            node.next_node = pre
            pre = node
            node = tmp
        self.__head.next_node = None
        self.__head = pre

    def has_ring(self) -> bool:
        """
        检查单链表是否存在环
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        :return:
            True:有环
            False:没有环
        """
        if self.__head is None:
            return False
        fast = self.__head
        slow = self.__head
        while (fast is not None) and (fast.next_node is not None):
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True
        return False
