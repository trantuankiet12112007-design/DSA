class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list_iterative(head_node):
    prev = None
    curr = head_node
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head = reverse_linked_list_iterative(head)

res = []
c = head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 6 (LL):", " -> ".join(res))