class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_cycle_start(head_node):
    slow = head_node
    fast = head_node
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    slow = head_node
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow



head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node2
node2.next = node3
node3.next = node2

start_node = detect_cycle_start(head)
print("Bài 12 (LL) - Vòng lặp bắt đầu tại nút:", start_node.data)