#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = []
        queue = [[root, 0]]
        while queue:
            handle = queue.pop(0)
            if not handle[0]:
                pass
            else:
                queue.append([handle[0].left, handle[1] + 1])
                queue.append([handle[0].right, handle[1] + 1])
                try:
                    res[handle[1]].append(handle[0])
                    res[handle[1]][-2].next = res[handle[1]][-1]
                except:
                    res.append([handle[0]])
        return root
# @lc code=end

