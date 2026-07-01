class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_kth_from_end(head_node, k):
    dummy = Node(0)
    dummy.next = head_node
    first = dummy
    second = dummy

    for _ in range(k + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = remove_kth_from_end(head, k=2)

res = []
c = head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 10 (LL):", " -> ".join(res))