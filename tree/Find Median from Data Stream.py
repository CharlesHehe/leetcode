class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        sum = 0
        for i in self.l:
            sum += i
        return sum / len(self.l)


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
param_2 = obj.findMedian()
