#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        handleA = ListNode()
        handleA.next = headA
        handleB = ListNode()
        handleB.next = headB
        sizeA, sizeB = 0, 0
        while headA:
            headA = headA.next
            sizeA += 1
        while headB:
            headB = headB.next
            sizeB += 1
        if sizeA>sizeB:
            longerHead = handleA.next
            shoterHead = handleB.next
        else:
            longerHead = handleB.next
            shoterHead = handleA.next
        for _ in range(max(sizeA, sizeB)-min(sizeA, sizeB)):
            longerHead = longerHead.next
        while longerHead:
            if longerHead == shoterHead:
                return longerHead
            longerHead, shoterHead = longerHead.next, shoterHead.next
        return None
# @lc code=end