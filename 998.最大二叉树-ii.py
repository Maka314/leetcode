#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(tree, newNode):
            if not tree:
                return newNode
            elif val > tree.val:
                newNode.left = tree
                return newNode
            else:
                tree.right = insert(tree.right, newNode)
                return tree
        newNode = TreeNode(val)
        return insert(root, newNode)
# @lc code=end

