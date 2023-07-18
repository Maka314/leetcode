#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetricCheck(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return symmetricCheck(left.left, right.right) and symmetricCheck(
                    left.right, right.left
                )

        return symmetricCheck(root.left, root.right)


# @lc code=end
