#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def constructor(preorder,inorder):
            if not preorder:
                return None
            val = preorder[0]
            node = TreeNode(val)
            i = inorder.index(val)
            node.left = constructor(preorder[1:i+1], inorder[:i])
            node.right = constructor(preorder[i+1:], inorder[i+1:])
            return node
        
        return constructor(preorder,inorder)
# @lc code=end

