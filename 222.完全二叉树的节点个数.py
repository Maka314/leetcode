#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        nodeList = [root]
        while nodeList:
            res += 1
            currentNode = nodeList.pop(0)
            if currentNode.left:
                nodeList.append(currentNode.left)
            if currentNode.right:
                nodeList.append(currentNode.right)
        return res
# @lc code=end

