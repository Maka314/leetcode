#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.ticketBook = {}
        self.res = ["JFK"]
        ticketCount = len(tickets)

        for ticket in tickets:
            if ticket[0] in self.ticketBook:
                self.ticketBook[ticket[0]].append([ticket[1], 1])
            else:
                self.ticketBook[ticket[0]] = [[ticket[1], 1]]

        for startP in self.ticketBook:
            self.ticketBook[startP].sort()
        
        print(self.ticketBook)

        self.backTracking("JFK", ticketCount)
        return self.res

    def backTracking(self, currentAirport, ticketCount):
        if ticketCount == 0:
            return True

        if currentAirport not in self.ticketBook:
            return

        for ticketNumber in range(len(self.ticketBook[currentAirport])):
            if self.ticketBook[currentAirport][ticketNumber][1]:  # 遍历该机场可用机票
                self.ticketBook[currentAirport][ticketNumber][1] = 0
                self.res.append(self.ticketBook[currentAirport][ticketNumber][0])
                result = self.backTracking(
                    self.ticketBook[currentAirport][ticketNumber][0], ticketCount - 1
                )
                if result:
                    return True
                self.res.pop()
                self.ticketBook[currentAirport][ticketNumber][1] = 1
        return


# @lc code=end
