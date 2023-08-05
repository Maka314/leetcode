#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        handle = res
        while list1:
            if list2 and list1.val >= list2.val:
                handle.next = list2
                list2 = list2.next
                handle = handle.next
            else:
                handle.next = list1
                list1 = list1.next
                handle = handle.next
        handle.next = list2
        return res.next
# @lc code=end

