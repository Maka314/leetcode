#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastHandle = head
        slowHandle = head
        while slowHandle:
            if not fastHandle.next or not fastHandle.next.next:
                return False
            fastHandle = fastHandle.next.next
            slowHandle = slowHandle.next
            if fastHandle == slowHandle:
                return True
        return False
# @lc code=end

