
'''
Given an array of positive integers and a number ‘S,’
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0 if no such subarray exists.

'''


def smallest_subarray_with_given_sum(s, arr):
    window_start = 0
    min_len = float("inf")
    curr_sum = 0
    for window_end in range(len(arr)):
        curr_sum += arr[window_end]
        if curr_sum>=s:
            while curr_sum>=s:
                min_len=min(min_len, 1+window_end-window_start)
                curr_sum-=arr[window_start]
                window_start+=1
    return min_len

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
