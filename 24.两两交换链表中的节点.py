#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        handle = res
        while head and head.next:
            handle.next = head.next
            temp = head
            head = head.next.next
            temp.next = None
            handle.next.next = temp
            handle = handle.next.next
        if head:
            handle.next = head
        return res.next

# @lc code=end

