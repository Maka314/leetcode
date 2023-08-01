#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        nodeList = []
        usedCount = {}
        while head:
            nodeList.append(head)

            if head.val in usedCount:
                usedCount[head.val] += 1
            else:
                usedCount[head.val] = 1
            head = head.next
            nodeList[-1].next = None
        
        res = ListNode()
        head = res
        for node in nodeList:
            if usedCount[node.val] == 1:
                head.next = node
                head = head.next
        
        return res.next
# @lc code=end

