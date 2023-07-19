#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root):
            if not root:
                return 0
            leftHigh = balance(root.left)
            rightHigh = balance(root.right)
            if abs(leftHigh-rightHigh)>1:
                return -1
            else:
                return max([leftHigh,rightHigh])+1
        
        if balance(root) == -1:
            return False
        else:
            return True
# @lc code=end

