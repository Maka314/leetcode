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
        handle=ListNode()
        w = handle
        while head:
            if not head.next:
                w.next = head
                head = head.next
            else:
                w.next = head.next
                head.next = head.next.next
                w.next.next = head
                w = w.next.next
                head = head.next
        return handle.next
# @lc code=end

