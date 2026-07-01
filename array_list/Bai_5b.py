class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_by_value(head_node, x):
    if not head_node:
        return None
    if head_node.data == x:
        return head_node.next

    curr = head_node
    while curr.next:
        if curr.next.data == x:
            curr.next = curr.next.next
            return head_node
        curr = curr.next
    return head_node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head = remove_by_value(head, 2)

res = []
c = head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 5 (LL):", " -> ".join(res))