#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def pathFinder(root,path):
            if not root.left and not root.right:
                return path + 1
            son = []
            if root.left:
                son.append(pathFinder(root.left,path + 1))
            if root.right:
                son.append(pathFinder(root.right,path + 1))
            print()
            return min(son)
        if not root:
            return 0
        return pathFinder(root,0)
# @lc code=end

