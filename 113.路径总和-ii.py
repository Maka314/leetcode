#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if root.val == targetSum and not root.left and not root.right:
            return [[root.val]]

        leftRes = self.pathSum(root.left, targetSum - root.val)
        rightRes = self.pathSum(root.right, targetSum - root.val)
        res = []
        for i in (leftRes + rightRes):
            res.append([root.val]+i)
        return res
# @lc code=end

