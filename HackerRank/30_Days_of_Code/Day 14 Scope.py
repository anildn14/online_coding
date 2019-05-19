class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        # self.maximumDifference=0
        # for x in self.__elements:
        #     self.maximumDifference=abs(x-self.maximumDifference)
        # print self.maximumDifference
        self.max=max(self.__elements)
        self.min=min(self.__elements)
        self.maximumDifference=abs(self.max-self.min)
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference

#Actual Solution:

#self.maximumDifference = max(a) - min(a)
