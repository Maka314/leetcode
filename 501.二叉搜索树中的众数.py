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
        def minScarch(root):
            if not root:
                return []
            res = []
            res += minScarch(root.left)
            res.append(root.val)
            res += minScarch(root.right)
            return res
        queue = minScarch(root)
        numSet = set()
        biggestCount = 0
        res = []
        for i in queue:
            if i not in numSet:
                numSet.add(i)
                if queue.count(i) > biggestCount:
                    res = [i]
                    biggestCount = queue.count(i)
                elif queue.count(i) == biggestCount:
                    res.append(i)
        return res
# @lc code=end

