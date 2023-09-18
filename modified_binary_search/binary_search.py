
'''
Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

Input: [4, 6, 10], key = 10
Output: 2
'''



def binary_search(arr, key):
    is_ascending = True
    start = 0
    end = len(arr)-1
    if arr[start] > arr[end]:
        is_ascending=False


    while start<=end:
        mid = start + (end-start)//2
        # print(mid)
        if key == arr[mid]:
            return mid
        if key>arr[mid]:
            if is_ascending: start=mid+1
            else:end = mid-1
        else:
            if is_ascending: end = mid-1
            else: start=mid+1
    return -1

def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()


