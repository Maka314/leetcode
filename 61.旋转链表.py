#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        handle = ListNode()
        handle.next = head
        size = 1
        while head.next!=None:
            size+=1
            head = head.next
        realK = k%size
        if realK==0:
            return handle.next
        head.next = handle.next
        head = head.next
        for i in range(size-realK):
            if i == size-realK-1:
                res = head.next
                head.next = None
                return res
            head = head.next
# @lc code=end

