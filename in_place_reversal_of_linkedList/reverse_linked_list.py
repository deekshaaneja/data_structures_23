

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        ls = []
        curr = self
        while curr:
            ls.append(str(curr.value))
            curr=curr.next
        print("->".join(ls))


def reverse(head):
    prev = None
    curr = head
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr=next
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()