from heapq import *

class MedianOfAStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median=None

    def insert_num(self, num):
        if self.max_heap and num>-self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap)+1:
            x = -heappop(self.max_heap)
            heappush(self.min_heap, x)

        if len(self.min_heap) > len(self.max_heap):
            x = heappop(self.min_heap)
            heappush(self.max_heap, -x)

    def find_median(self):
        print(self.max_heap, self.min_heap)
        if len(self.max_heap)> len(self.min_heap):
            return -self.max_heap[0]
        return self.min_heap[0]/2 - self.max_heap[0]/2



def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()