#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            currentNode = stack.pop()
            res.append(currentNode.val)
            if currentNode.left:
                stack.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
        return res[::-1]
# @lc code=end

