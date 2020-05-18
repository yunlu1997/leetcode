"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
两次遍历，第一次找到长度L
第二次找到L-n，将L-n+1个节点删除即可
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)   # 创建哑节点
        dummy.next = head
        first = ListNode(0)   # 第一次遍历
        first.next = head
        length = 0
        while first.next is not None:   # 遍历整个链表，记录length
            length += 1
            first = first.next
        target = length - n
        first = dummy
        while target > 0:   # 第二次从哑节点开始遍历，遍历至length - n 个节点
            first = first.next
            target -= 1
        first.next = first.next.next
        return dummy.next

"""
一次遍历
双指针法
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)  # 创建哑节点
        dummy.next = head
        fast,slow = dummy,dummy  # 创建快指针和慢指针
        for i in range(n):
            fast = fast.next
        while fast.next is not None:  # 接着遍历至链表尾部
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # 删除slow的后一个节点
        return dummy.next


