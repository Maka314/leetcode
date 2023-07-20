#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                replaceNode = root.right
                while replaceNode.left:
                    replaceNode = replaceNode.left
                replaceNode.left = root.left
                return root.right
            elif root.left:
                return root.left
            else:
                return root.right
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)

        return root

# @lc code=end

