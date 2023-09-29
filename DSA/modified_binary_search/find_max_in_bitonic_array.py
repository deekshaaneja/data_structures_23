


def find_max_in_bitonic_array(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        mid = start+ (end-start)//2
        if arr[start]<arr[mid]<arr[end]:
            return arr[end]
        elif arr[mid]>arr[start] and arr[mid]>arr[end]:
            start=mid+1
        else:
            end=mid-1

    return arr[start]



def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()