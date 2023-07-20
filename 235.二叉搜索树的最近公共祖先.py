#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root == p or root == q or root == None:
            return root

        leftResult = (
            None
            if (root.val < p.val and root.val < q.val)
            else self.lowestCommonAncestor(root.left, p, q)
        )
        rightResult = (
            None
            if (root.val > p.val and root.val > q.val)
            else self.lowestCommonAncestor(root.right, p, q)
        )

        if not leftResult and not rightResult:
            return None
        elif leftResult and rightResult:
            return root
        elif rightResult:
            return rightResult
        else:
            return leftResult
# @lc code=end
