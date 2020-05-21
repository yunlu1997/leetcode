"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

通过次数88,659提交次数212,041

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
利用堆栈，两次遍历。
第一次入栈
第二次出栈并比较
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        move = head # 建立游标
        while move:
            stack.append(move) # 进栈
            move = move.next
        move_ = head # 第二次的游标
        while move_:
            temp = stack.pop() # 出栈
            if move_.val != temp.val:
                return False
            move_ = move_.next
        return True


