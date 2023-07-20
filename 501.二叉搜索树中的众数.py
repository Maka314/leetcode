#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        elementDict = {}
        def elementSearch(root):
            if not root:
                return 0
            if root.val in elementDict:
                elementDict[root.val] += 1
            else:
                elementDict[root.val] = 1
            elementSearch(root.left)
            elementSearch(root.right)
        elementSearch(root)
        m = 0
        for i in elementDict:
            if elementDict[i] > m:
                res = [i]
                m = elementDict[i]
            elif elementDict[i] == m:
                res += [i]
        return res
# @lc code=end

