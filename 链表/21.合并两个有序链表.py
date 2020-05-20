"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) # 建立哑节点
        move = dummy
        while l1 and l2: # 遍历l1 和 l2
            if l1.val < l2.val: # l1 比 l2小时， 游标的下个节点为l1, 并且l1向右移动一个
                move.next = l1
                l1 = l1.next
                move = move.next # 游标也要移动一位
            else:               # 反之，游标下个节点为l2, 并且l2向右移动一个
                move.next = l2
                l2 = l2.next
                move = move.next
            # 处理剩余的链表
        if l1:
            move.next = l1
        if l2:
            move.next = l2
        return dummy.next