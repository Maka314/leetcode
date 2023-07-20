#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def minSearch(root):
            if not root:
                return []
            res = []
            res += minSearch(root.left)
            res.append(root.val)
            res += minSearch(root.right)
            return res

        queue = minSearch(root)
        res = queue[1] - queue[0]
        for i in range(1, len(queue)):
            res = min(res, queue[i] - queue[i - 1])
        return res


# @lc code=end
