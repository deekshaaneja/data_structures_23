
from heapq import *

def find_Kth_smallest(lists, k):
    min_heap = []
    for elem in lists:
        heappush(min_heap, (elem[0], 0, elem))

    while min_heap:
        num, index, ls = heappop(min_heap)
        k-=1
        if k == 0:
            return num
        next_index = index+1
        if next_index<len(ls):
            heappush(min_heap, (ls[next_index], next_index, ls))
    return -1



def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()
