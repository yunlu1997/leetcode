"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)     # 建立哑节点作为结果链表的开头
        move = dummy  # 建立移动游标
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1  # 游标指向l1
                l1 = l1.next    # l1指向下个节点

            else:
                move.next = l2  # 游标指向l2
                l2 = l2.next  # l2指向下个节点

            move = move.next    # 移动游标向后移动一位

        if l1:  # 未遍历完的则接在结果链表之后
            move.next = l1
        if l2:
            move.next = l2

        return dummy.next








