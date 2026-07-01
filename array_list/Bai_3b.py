class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_linked_list(head_node, target):
    index = 0
    curr = head_node
    while curr:
        if curr.data == target:
            return index
        curr = curr.next
        index += 1
    return -1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Bài 3 (LL) - Vị trí của số 2:", search_linked_list(head, 2))