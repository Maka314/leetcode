#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def treeList(left, right):
            if right - left == 1:
                return [None]
            if right - left == 2:
                return [TreeNode(right - 1)]

            res = []
            for rootValue in range(left + 1, right):
                leftTreeList = treeList(left, rootValue)
                rightTreeList = treeList(rootValue, right)
                for leftTree in leftTreeList:
                    for rightTree in rightTreeList:
                        res.append(TreeNode(rootValue, leftTree, rightTree))
            return res

        return treeList(0, n + 1)


# @lc code=end
