class SmallestInfiniteSet:

    def __init__(self):
        self.lowerBond = 1
        self.afterLife = set()


    def popSmallest(self) -> int:
        if self.afterLife:
            removeTarget = min(self.afterLife)
            self.afterLife.remove(removeTarget)
            res = removeTarget
        else:
            res = self.lowerBond
            self.lowerBond += 1
        return res



    def addBack(self, num: int) -> None:
        if num not in self.afterLife and num < self.lowerBond:
            self.afterLife.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)