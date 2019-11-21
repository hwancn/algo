# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = head
        cur = head.next
        while (cur):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next = None
        return pre
