#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(root):
            if not root:
                return None
            else:
                root.left,root.right = root.right,root.left
                flip(root.left)
                flip(root.right)
            return root
        return flip(root)
# @lc code=end

