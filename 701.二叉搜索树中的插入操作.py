#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        handle = root
        if not root:
            return TreeNode(val)
        while True:
            if val > handle.val:
                if handle.right:
                    handle = handle.right
                else:
                    handle.right = TreeNode(val)
                    return root
            else:
                if handle.left:
                    handle = handle.left
                else:
                    handle.left = TreeNode(val)
                    return root
# @lc code=end

