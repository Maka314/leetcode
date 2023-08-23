#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        nodeList = []
        left -= 1
        right -= 1

        while head:
            nodeList.append(head)
            head = head.next
            nodeList[-1].next = None

        res = ListNode()
        head = res
        for i in range(left):
            head.next = nodeList[i]
            head = head.next

        for i in range(right, left - 1, -1):
            head.next = nodeList[i]
            head = head.next

        for i in range(right + 1, len(nodeList)):
            head.next = nodeList[i]
            head = head.next

        return res.next


# @lc code=end
