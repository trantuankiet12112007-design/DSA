class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_length_and_print(head_node):
    count = 0
    curr = head_node
    print("Các nút: ", end="")
    while curr:
        print(curr.data, end=" ")
        count += 1
        curr = curr.next
    print()
    return count

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print("Bài 2 (LL) - Độ dài:", get_length_and_print(node1))