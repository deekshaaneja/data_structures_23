
from heapq import *

def find_Kth_smallest(matrix, k):
    min_heap=[]
    for row in matrix:
        heappush(min_heap, (row[0], 0, row))

    while min_heap:
        num, idx, row = heappop(min_heap)
        k-=1
        if k==0:
            return num
        next_idx = idx+1
        if next_idx<len(row):
            heappush(min_heap, (row[next_idx], next_idx, row))

def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()

