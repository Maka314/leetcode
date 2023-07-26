#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.nodeCheck(root)
        if root.val == 0:
            self.res += 1
        return self.res
    
    def nodeCheck(self, node):
        if not node:
            return
        
        self.nodeCheck(node.left)
        self.nodeCheck(node.right)

        if (node.left and node.left.val == 0) or (node.right and node.right.val == 0):
            node.val = 2
            self.res += 1
            return
        elif (node.left and node.left.val == 2) or (node.right and node.right.val == 2):
            node.val = 1
            return
# @lc code=end

