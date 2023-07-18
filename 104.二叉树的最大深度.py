#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def pathFinder(root, path):
            if not root:
                return path
            else:
                return max(pathFinder(root.left,path + 1),pathFinder(root.right,path+1))
        
        return pathFinder(root,0)
# @lc code=end

