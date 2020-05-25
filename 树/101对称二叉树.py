"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""递归"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(left,right):
            if  (left == None and right == None):  # 上一节点为叶子节点
                return True
            if (left == None and right != None) or (left != None and right==None ):   # 上一节点的左右有一个空节点
                return False
            if left.val != right.val:   # 左右不相等
                return False
            #   递归
            return dfs(left.left,right.right) and dfs(left.right, right.left)
        return dfs(root.left,root.right)
