# 链表中两数相加
# 时间复杂度O(n), 空间复杂度O(n)
# 代码还可以再整合一下，把相似的逻辑单独拎出来整合下

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        flag = False
        val = l1.val + l2.val
        if val >=10:
            l3 = ListNode(val-10)
            flag = True
        else:
            l3 = ListNode(val)
        l1 = l1.next
        l2 = l2.next
        root = l3
        while (l1 is not None and l2 is not None):
            val = l1.val + l2.val
            if flag:
                val += 1
            l1 = l1.next
            l2 = l2.next
            if val >= 10:
                tail = ListNode(val-10)
                flag = True
            else:
                tail = ListNode(val)
                flag = False
            l3.next = tail
            l3 = tail
        if l1 is None:
            while l2 is not None:
                val = l2.val
                if flag:
                    val += 1
                if val >= 10:
                    tail = ListNode(val-10)
                    flag = True
                else:
                    tail = ListNode(val)
                    flag = False
                l3.next = tail
                l3 = tail
                l2 = l2.next
        if l2 is None:
            while l1 is not None:
                val = l1.val
                if flag:
                    val += 1
                if val >= 10:
                    tail = ListNode(val-10)
                    flag = True
                else:
                    tail = ListNode(val)
                    flag = False
                l3.next = tail
                l3 = tail
                l1 = l1.next
        if flag:
            tail = ListNode(1)
            l3.next = tail
        return root
        
