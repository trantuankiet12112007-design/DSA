class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_after_node(head_node, target_val, new_val):
    curr = head_node
    while curr:
        if curr.data == target_val:
            new_node = Node(new_val)
            new_node.next = curr.next
            curr.next = new_node
            return head_node
        curr = curr.next
    return head_node


head = Node(1)
head.next = Node(3)
head = insert_after_node(head, target_val=1, new_val=2)

res = []
c = head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 4 (LL):", " -> ".join(res))