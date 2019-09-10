# -*- coding: utf-8 -*-
"""
基于数组实现的队列
此处为了简便使用Python的列表
"""


class ArrayQueue:

    def __init__(self, capacity: int):
        self._item = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        """
        入队列
        :param item: 队列元素, 假设元素是字符串
        :return: True or False True表示入队成功，False表示失败
        """
        # 示例代码中_tail实际上指向的是最后一个节点的下一个位置，也可以指向最后一个节点的位置，
        if self._tail == self._capacity:
            # 到了数组尾部
            if self._head == 0:
                # 队列满了
                return False
            else:
                # 转移数据
                # self._tail-self._head 边界问题注意下， self._tail是不存储数据的，此时等于self._capacity
                for i in range(0, self._tail-self._head):
                    # 转移数据，其实原来的位置还是存储着原来的数据，此处暂时不处理
                    self._item[i] = self._item[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        # 入队列
        self._item.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> str:
        if self._head != self._tail:
            # 队列不为空
            item = self._item[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self):
        return ' '.join(item for item in self._item[self._head: self._tail])


if __name__ == '__main__':
    aq = ArrayQueue(capacity=3)
    aq.enqueue('a')
    print(aq)
    aq.enqueue('b')
    print(aq)
    aq.enqueue('c')
    print(aq)
    aq.enqueue('d')
    print(aq)
    aq.dequeue()
    print(aq)
    aq.enqueue('d')
    print(aq)
# a
# a b
# a b c
# a b c
# b c
# b c d
