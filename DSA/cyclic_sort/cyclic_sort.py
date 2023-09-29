'''
Write a function to sort the objects in-place on their creation sequence number in O(n)
 and without using any extra space.
 For simplicity, let’s assume we are passed an integer array containing only the sequence numbers,
 though each number is actually an object.
 [3, 1, 5, 4, 2]
  [1, 5, 6, 4, 3, 2]
'''


def cyclic_sort(nums):
    i=0
    while i<len(nums):
        j = nums[i]-1
        if j != i:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

