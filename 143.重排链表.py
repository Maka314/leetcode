#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodeList = []
        while head:
            nodeList.append(head)
            head = head.next
            nodeList[-1].next = None
        left = 0
        right = len(nodeList) - 1
        while (right - left) > 1:
            print(right - left)

            nodeList[left].next = nodeList[right]
            nodeList[right].next = nodeList[left + 1]

            left += 1
            right -= 1
        if right - left:
            nodeList[left].next = nodeList[right]
# @lc code=end

