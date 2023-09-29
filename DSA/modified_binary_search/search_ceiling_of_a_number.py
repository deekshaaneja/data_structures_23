





def search_ceiling_of_a_number(arr, key):
    if key>arr[-1]:
        return -1
    start = 0
    end = len(arr)-1
    mid = -1
    while start<end:
        mid = start+ (end-start)//2
        if key==arr[mid]:
            return mid
        elif arr[mid]>key:
            end = mid-1
        else:
            start=mid+1
    return start



def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()