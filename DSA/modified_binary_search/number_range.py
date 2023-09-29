
'''
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.


'''
def binary_search(arr, key, find_max_index=True):
    start = 0
    end = len(arr)-1
    keyIndex=-1
    while start <= end:
        mid = start + (end-start)//2
        if key>arr[mid]:
            start=mid+1
        elif key<arr[mid]:
            end = mid -1
        else:
            keyIndex = mid
            if find_max_index:
                start=mid+1
            else:
                end = mid-1
    return keyIndex

def find_range(arr, key):
    start = binary_search(arr, key, False)
    end= binary_search(arr, key)
    return [start, end]


def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()


