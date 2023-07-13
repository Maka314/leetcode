#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums):
            if not nums:
                return None
            elif len(nums) == 1:
                return TreeNode(val=nums[0])
            else:
                bigI = nums.index(max(nums))
                leftNode = buildTree(nums[:bigI])
                rightNode = buildTree(nums[bigI+1:])
                currentNode = TreeNode(nums[bigI],leftNode,rightNode)
                return currentNode
        
        return buildTree(nums)
# @lc code=end

