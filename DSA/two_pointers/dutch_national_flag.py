
'''
Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]

'''


def dutch_flag_sort(arr):
    start = 0
    end = len(arr)-1
    current_index = 0
    while current_index<=end:
        if arr[current_index]==0:
            arr[start], arr[current_index] = arr[current_index], arr[start]
            start+=1
            current_index+=1
        elif arr[current_index]==2:
            arr[end], arr[current_index] = arr[current_index], arr[end]
            end-=1
        else:
            current_index+=1
    return arr

def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()

