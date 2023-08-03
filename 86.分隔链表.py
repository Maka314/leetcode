#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallHandle = ListNode()
        s = smallHandle
        bigHandle = ListNode()
        b = bigHandle
        while head:
            tempNode = head
            head = head.next
            tempNode.next = None
            if tempNode.val < x:
                s.next = tempNode
                s = s.next
            else:
                b.next = tempNode
                b = b.next
        s.next = bigHandle.next
        return smallHandle.next
# @lc code=end

