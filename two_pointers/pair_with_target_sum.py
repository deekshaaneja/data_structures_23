'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

'''

def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) -1
    while start<end:
        if arr[start]+arr[end] > target_sum:
            end-=1
        elif arr[start]+arr[end] < target_sum:
            start+=1
        else:
            return start, end
    return -1, -1

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
