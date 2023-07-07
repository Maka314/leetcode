#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.handle = ListNode()
        self.count = 0

    def show(self) -> None:
        operator = self.handle
        queue = []
        while operator.next != None:
            queue.append(operator.next.val)
            operator = operator.next
        print(queue)

    def get(self, index: int) -> int:
        self. show()
        if index < 0:
            return -1
        handle = self.handle.next
        while index > 0 and handle != None:
            handle = handle.next
            index -= 1
        if handle == None:
            return -1
        else:
            return handle.val

    def addAtHead(self, val: int) -> None:
        addOne = ListNode(val = val, next= self.handle.next)
        self.handle.next = addOne
        self.count += 1

    def addAtTail(self, val: int) -> None:
        operator = self.handle
        addOne = ListNode(val = val)
        for i in range(self.count):
            operator = operator.next
        operator.next = addOne
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.count:
            return 0
        operator = self.handle
        addOne = ListNode(val = val)
        for i in range(index):
            operator = operator.next
        addOne.next = operator.next
        operator.next = addOne
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index+1>self.count:
            return 0
        operator = self.handle
        for i in range(index):
            operator = operator.next
        operator.next = operator.next.next
        self.count -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

