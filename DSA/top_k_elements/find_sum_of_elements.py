from heapq import *
'''
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

'''

def find_sum_of_elements(nums, k1, k2):
    max_heap = []
    for i in range(len(nums)):
        if len(max_heap)<k2-1:
            heappush(max_heap, -nums[i])
        elif -max_heap[0]>nums[i]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    print(max_heap)
    s= 0
    while k1<k2-1:
        num = -heappop(max_heap)
        s+=num
        k2-=1
    return s


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()