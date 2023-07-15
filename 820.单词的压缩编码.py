#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#


# @lc code=start
class treeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = {}

    def addNode(self, node):
        self.next[node.val] = node

    def findNode(self, val):
        if val in self.next:
            return self.next[val]
        else:
            return None


class compressTree:
    def __init__(self) -> None:
        self.root = treeNode(0)

    def addWord(self, word):
        operator = self.root
        for i in word[::-1]:
            nextNode = operator.findNode(i)
            if nextNode:
                operator = nextNode
            else:
                nextNode = treeNode(i)
                operator.addNode(nextNode)
                operator = nextNode

    def countTree(self, node: treeNode, layer=0):
        res = 0
        if not node.next:
            return layer + 1
        else:
            res = 0
            for i in node.next:
                res += self.countTree(node.next[i],layer+1)
            return res


class Solution:
    def minimumLengthEncoding(self, words) -> int:
        res = compressTree()
        for w in words:
            res.addWord(w)
        return(res.countTree(res.root))
# @lc code=end
