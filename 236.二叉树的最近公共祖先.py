#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 本题创新在于递归解可以返回不只一种数据结构，
        # 这一题就可以返回节点或者None
        # 不过其实还是对题意理解有问题
        if root == p or root == q or not root:
            return root
        
        leftResult = self.lowestCommonAncestor(root.left, p, q)
        rightResult = self.lowestCommonAncestor(root.right, p, q)

        if not leftResult and not rightResult:
            return None
        elif leftResult and rightResult:
            return root
        elif rightResult:
            return rightResult
        else:
            return leftResult
# @lc code=end

