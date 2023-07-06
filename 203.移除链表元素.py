 #
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        handle = ListNode()
        operation = handle

        while head!=None:
            if head.val == val:
                head = head.next
            else:
                operation.next = head
                operation = operation.next
                head = head.next
        operation.next=None
        return handle.next
# @lc code=end

