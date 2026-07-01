# Cấu trúc nút liên kết đôi (có prev và next)
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, x):
        new_node = DoublyNode(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_forward(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return " -> ".join(res)

dll = DoublyLinkedList()
dll.push_back(10)
dll.push_back(20)
print("Bài 11 (LL) - Duyệt xuôi:", dll.display_forward())