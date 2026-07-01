class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head_node):
    slow = head_node
    fast = head_node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = head

print("Bài 8 (LL) - Có chu trình không?:", has_cycle(head))