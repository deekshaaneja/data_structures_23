from  heapq import *

'''
Given two sorted arrays in descending order,
find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

'''


def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    for i in range(min(len(nums1), k)):
        for j in range(min(len(nums2), k)):
            if len(min_heap)<k:
                heappush(min_heap, ((nums1[i])+nums2[j], i, j))
            elif len(min_heap)==k and min_heap[0][0] < nums1[i] + nums2[j]:
                heappop(min_heap)
                heappush(min_heap, ((nums1[i]) + nums2[j], i, j))

    result = []
    while min_heap:
        sum_num, idx1, idx2 = heappop(min_heap)
        result.append((nums1[idx1], nums2[idx2]))
    return result

def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))

  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([5, 2, 1], [2, -1], 3)))


main()





