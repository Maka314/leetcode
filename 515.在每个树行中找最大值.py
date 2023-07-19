#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [[root, 0]]
        while queue:
            handle = queue.pop(0)
            if not handle[0]:
                pass
            else:
                queue.append([handle[0].left, handle[1] + 1])
                queue.append([handle[0].right, handle[1] + 1])
                try:
                    res[handle[1]].append(handle[0].val)
                except:
                    res.append([handle[0].val])
        for i in range(len(res)):
            res[i] = max(res[i])
        return res
# @lc code=end

