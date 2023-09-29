
'''Given an array of numbers sorted in ascending order,
find the element in the array that has the minimum difference with the given ‘key’.

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
'''

def search_min_diff_element(arr, key):
    start = arr[0]
    end = len(arr)-1
    if key<arr[start]:
        return arr[start]
    if key>arr[end]:
        return arr[end]

    while start<=end:
        mid=start+(end-start)//2
        if key==arr[mid]:
            return arr[mid]
        elif key>arr[mid]:
            end=mid-1
        else:
            start=mid+1
    if abs(arr[start]-key) > abs(arr[end]-key):
        return arr[start]
    return arr[end]







