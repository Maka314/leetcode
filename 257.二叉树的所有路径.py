#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def router(root):
            res = []
            if not root.left and not root.right:
                res.append(str(root.val))
            else:
                if root.left:
                    tempRes = router(root.left)
                    for i in tempRes:
                        res.append(str(root.val)+"->"+i)
                if root.right:
                    tempRes = router(root.right)
                    for i in tempRes:
                        res.append(str(root.val)+"->"+i)
            return res
        
        return router(root)
# @lc code=end

