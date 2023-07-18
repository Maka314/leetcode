#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pTraversal(root):
            if not root:
                return []
            res = []
            res += pTraversal(root.left)
            res += [root.val]
            res += pTraversal(root.right)
            return res

        return pTraversal(root)
# @lc code=end

