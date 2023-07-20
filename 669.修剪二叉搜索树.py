#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.right = self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)

        if root.val < low:
            return root.right
        if root.val > high:
            return root.left
        
        return root
# @lc code=end

