"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


"""广度优先搜索"""
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)  # 将根节点加入队列
        res = []
        while queue:
            size = len(queue)
            level = []  # 用于存储本层的结果列表
            for _ in range(size):   # 遍历当前队列
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left)  # 将左右子节点加入队列
                    queue.append(cur.right)
                    level.append(cur.val)   # 将当前节点值加入此层的结果列表
            if level:
                res.append(level)   # 将本层的结果加入最终的结果列表
        return res

