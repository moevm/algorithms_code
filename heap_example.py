class Heap:
    def __init__(self):
        self.MAX_SIZE = 20
        self.heap = [None] * self.MAX_SIZE
        self.size = 0

    @staticmethod
    def get_parent(index):
        return (index - 1) // 2

    @staticmethod
    def get_left_child(index):
        return 2 * index + 1

    @staticmethod
    def get_right_child(index):
        return 2 * index + 2

    def insert(self, element):
        if self.size == self.MAX_SIZE:
            return -1
        self.heap[self.size] = element
        self.sift_up(self.size)
        self.size += 1

    def extract_max(self):
        max_element = self.heap[0]
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], None
        self.size -= 1
        self.sift_down(0)
        return max_element

    def sift_up(self, index):
        parent = self.get_parent(index)
        while index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = self.get_parent(index)

    def sift_down(self, index):
        left = self.get_left_child(index)
        right = self.get_right_child(index)
        if left >= self.size and right >= self.size:
            return
        if right >= self.size:
            max_index = left if self.heap[left] > self.heap[index] else index
        else:
            max_index = left if self.heap[left] > self.heap[right] else right
            max_index = max_index if self.heap[max_index] > self.heap[index] else index
        if max_index != index:
            self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
            self.sift_down(max_index)

    def __str__(self):
        return str(self.heap)


def main():
    heap = Heap()
    heap.insert(5)
    heap.insert(7)
    heap.insert(3)
    heap.insert(6)
    heap.insert(8)
    print(heap)
    heap.extract_max()
    print(heap)
    heap.extract_max()
    print(heap)


main()
