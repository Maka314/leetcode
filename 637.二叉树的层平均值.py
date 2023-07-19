#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        quene=deque()
        ans=[]
        if not root:
            return quene
        quene.append(root)
        while quene:
            n,length=len(quene),len(quene)
            temp=0
            while n:
                cur=quene.popleft()
                temp+=cur.val
                if cur.left:
                    quene.append(cur.left)
                if cur.right:
                    quene.append(cur.right)
                n-=1
            ans.append(temp/length)
        return ans
# @lc code=end

