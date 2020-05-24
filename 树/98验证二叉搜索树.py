"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs (node, min_val, max_val):
            if not node:    # 到了叶子节点
                return True
            if not min_val<node.val<max_val:    # 判断是否介于上下界之间
                return False
            # 该节点符合二叉搜索树，继续往下一个节点遍历
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root,float('-inf'), float('inf'))   # 根节点上下界是无穷