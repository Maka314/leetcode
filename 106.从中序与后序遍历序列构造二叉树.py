#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def constructor(postorder,inorder):
            if not postorder:
                return None
            val = postorder[-1]
            node = TreeNode(val)
            i = inorder.index(val)
            node.left = constructor(postorder[:i], inorder[:i])
            node.right = constructor(postorder[i:len(postorder)-1], inorder[i+1:])
            return node
        
        return constructor(postorder,inorder)
# @lc code=end

