#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] 二叉树中的链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root: return False
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 

    def helper(self, head, root):
        if not head:
            return True
        if root and root.val != head.val or not root:
            return False
        return self.helper(head.next, root.left) or self.helper(head.next, root.right)
# @lc code=end
