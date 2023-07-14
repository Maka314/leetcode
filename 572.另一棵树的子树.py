#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def juger(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return juger(p.left, q.left) and juger(p.right, q.right)
        
        def find(root,subRoot):
            if juger(root, subRoot):
                return True
            elif not root or not subRoot:
                return False
            else:
                res = find(root.right, subRoot) or find(root.left, subRoot)
                return res
        
        return find(root,subRoot)
# @lc code=end

