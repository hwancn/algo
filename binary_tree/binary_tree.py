# -*- coding: utf-8 -*-
"""
二叉查找树的常见操作
"""


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class BinarySearchTree:
    def __init__(self, val_list=[]):
        """
        :param val_list: 初始化列表
        """
        self.root = None
        for n in val_list:
            self.insert(n)

    def insert(self, data):
        """
        插入数据
        :param data: 插入值
        :return: True or False
        """
        if self.root is None:
            self.root = TreeNode(data)
        else:
            p = self.root
            while p:
                if data > p.val:
                    # 右子树
                    if p.right is None:
                        p.right = TreeNode(data)
                        return True
                    else:
                        p = p.right
                else:
                    # data < p.val， 不考虑相等的情况，即不考虑二叉查找树中有相同的元素
                    if p.left is None:
                        p.left = TreeNode(data)
                        return True
                    else:
                        p = p.left

    def search(self, target):
        """
        查找
        :param target:  目标数据
        :return: 节点或者None
        """
        p = self.root
        while p is not None:
            if p.val == target:
                return p
            elif p.val > target:
                # 左子树
                p = p.left
            else:
                # 右子树
                p = p.right
        return None

    def delete(self, target):
        """
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除该节点
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param target: 目标数据
        :return: True or False
        """
        pp, p = None, self.root  # p指向目标节点，指向目标节点的父节点
        while p is not None and p.val != target:
            pp = p
            if p.val > target:
                p = p.left
            else:
                p = p.right
        if p is None:
            # 没有找到
            return False
        # 有两个子节点
        if p.left is not None and p.right is not None:
            # 找到右子树的最小值
            min_p = p.right  # min_p指向右子树最小的节点
            min_pp = p   # min_pp指向min_p的父节点
            while min_p.left is not None:
                min_pp = min_p
                min_p = min_p.left
            p.val = min_p.val  # 将min_p的值替换到p中
            p = min_p   # 下面变成删除min_p了
            pp = min_pp

        # 待删除节点有一个子节点或者没有子节点
        # 获取p或者min_p的子节点，有可能有有可能没有，最多只有一个
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        if p == self.root:
            # 需要删除的节点是根节点
            self.root = child
        else:
            if pp.left == p:
                pp.left = child
            else:
                pp.right = child

    def _in_order(self, node):
        """
        中根遍历
        """
        if node is None:
            return []
        res = []
        res.extend(self._in_order(node.left))
        res.append(node.val)
        res.extend(self._in_order(node.right))
        return res

    def __repr__(self):
        # 此处只是简单的打印，如果需要准确的确定树形结构，至少需要中根和先根，或者中根和后根才可以确定
        return str(self._in_order(self.root))


if __name__ == '__main__':
    nums = [2, 5, 6, 1, 7, 3]
    bst = BinarySearchTree(nums)
    print(bst)
    print(bst.root)

    # 插入
    bst.insert(4)
    print(bst)

    # 搜索
    target_node = bst.search(2)
    print(target_node)

    bst.delete(7)
    print(bst)
    bst.delete(6)
    print(bst)
    bst.delete(2)
    print(bst)
    print(bst.root)

