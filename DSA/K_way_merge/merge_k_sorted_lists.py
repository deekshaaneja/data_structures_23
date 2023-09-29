from heapq import *

class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

    def __lt__(self, other):
        return self.value<other.value


def merge(lists):
    min_heap = []
    for elem in lists:
        heappush(min_heap, elem)
    head = curr= None
    while min_heap:
        elem = heappop(min_heap)
        print(elem.value)
        new_node = Node(elem.value)
        if not head:
            curr = new_node
            head = curr
        else:
            curr.next= new_node
            curr=curr.next
        if elem.next:
            heappush(min_heap, elem.next)
    return head

def main():
  l1 = Node(2)
  l1.next = Node(6)
  l1.next.next = Node(8)

  l2 = Node(3)
  l2.next = Node(6)
  l2.next.next = Node(7)

  l3 = Node(1)
  l3.next = Node(3)
  l3.next.next = Node(4)

  result = merge([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()



