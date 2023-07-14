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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def judge(root, head):
            if not root and not head:
                return True
            elif root and not head:
                return True
            elif not root or not head:
                return False
            if head.val == root.val:
                findRes = judge(root.left, head.next) or judge(root.right, head.next)
                if findRes:
                    return True
                else:
                    return judge(root.left, head) or judge(root.right, head)
            else:
                return judge(root.left, head) or judge(root.right, head)

        return judge(root, head)
# @lc code=end
