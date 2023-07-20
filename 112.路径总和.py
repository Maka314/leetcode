#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root.val == targetSum and not root.left and not root.right:
            return True
        
        leftTest = self.hasPathSum(root.left, targetSum - root.val)
        rightTest = self.hasPathSum(root.right, targetSum - root.val)
        return leftTest or rightTest
        
# @lc code=end

