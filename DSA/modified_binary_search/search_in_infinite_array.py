
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return float("inf") if index> len(self.arr) else self.arr[index]

def binary_search(start, end, reader, key):
    while start<end:
        mid = start+(end-start)//2
        min_num = reader.get(mid)
        if min_num==key:
            return mid
        elif key>min_num:
            start=mid+1
        else:
            end = mid-1
    return -1



def search_in_infinite_array(reader, key):
    current_num = 0
    prev_num=0
    while True:
        current_index = 2**current_num
        if key == reader.get(current_index):
            return current_index

        elif key>reader.get(current_index):
            prev_num=current_num
            current_num+=1
        else:
            return binary_search(2**prev_num, 2**current_num, reader, key)
    return -1





def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()