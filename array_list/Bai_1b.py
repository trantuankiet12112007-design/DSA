class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        res.append("null")
        return " -> ".join(res)

ll = SinglyLinkedList()
ll.push_front(2)
ll.push_back(5)
print("Bài 1 (LL):", ll.display())