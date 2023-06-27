#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        handle = ListNode()
        a = handle
        a.next = head
        a = a.next
        while head:
            if a.val!=head.val:
                a.next = head
                a=a.next
            head = head.next
        a.next = head
        return handle.next
# @lc code=end

