class FailFastArrayList:
    def __init__(self):
        self.data = []
        self.mod_count = 0

    def add(self, x):
        self.data.append(x)
        self.mod_count += 1

    def remove_last(self):
        if self.data:
            self.data.pop()
            self.mod_count += 1

    def __iter__(self):
        return self.ArrayListIterator(self)

    class ArrayListIterator:
        def __init__(self, list_obj):
            self.list_obj = list_obj
            self.cursor = 0
            self.expected_mod_count = list_obj.mod_count

        def __next__(self):
            if self.list_obj.mod_count != self.expected_mod_count:
                raise RuntimeError("Fail-Fast: Danh sách bị sửa đổi trong lúc duyệt!")
            if self.cursor >= len(self.list_obj.data):
                raise StopIteration
            res = self.list_obj.data[self.cursor]
            self.cursor += 1
            return res

my_list = FailFastArrayList()
my_list.add(10); my_list.add(20); my_list.add(30)

try:
    for item in my_list:
        print(item, end=" ")
        my_list.add(99)
except RuntimeError as e:
    print(f"\nBài 15 - Bắt lỗi thành công: {e}")