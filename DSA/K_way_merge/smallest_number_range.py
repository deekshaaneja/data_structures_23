
from heapq import *

def find_smallest_range(lists):
    min_heap=[]
    curr_max_num = -float("inf")
    rangeStart = 0
    rangeEnd = float("inf")
    for elem in lists:
        heappush(min_heap, (elem[0], 0, elem))
        curr_max_num = max(curr_max_num, elem[0])
    while len(min_heap)==len(lists):
        num, index, ls = heappop(min_heap)
        nex_idx = index+1

        if rangeEnd - rangeStart > curr_max_num - num:
            rangeStart=num
            rangeEnd=curr_max_num

        if nex_idx<len(ls):
            heappush(min_heap, (ls[nex_idx], nex_idx, ls))
            curr_max_num = max(curr_max_num, ls[nex_idx])




    return rangeStart, rangeEnd




def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()