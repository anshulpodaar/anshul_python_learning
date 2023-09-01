"""
Max Heaps
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print_heap(self):
        print(self.heap)

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and
                self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    for num in nums:
        max_heap.insert(num)
    while len(max_heap.heap) != k:
        max_heap.remove()
    return max_heap.remove()


def stream_max(nums):
    max_heap = MaxHeap()
    output_list = []
    for num in nums:
        max_heap.insert(num)
        max_val_so_far = max_heap.heap[0]
        output_list.append(max_val_so_far)
    return output_list


def _main():
    my_heap = MaxHeap()

    print("\n---------- insert method ----------")
    my_heap.insert(99)
    my_heap.insert(72)
    my_heap.insert(61)
    my_heap.insert(58)
    my_heap.print_heap()
    # print(my_heap.heap)

    my_heap.insert(100)
    my_heap.print_heap()

    my_heap.insert(75)
    my_heap.print_heap()

    print("\n---------- remove method ----------")
    max_val = my_heap.remove()
    print(max_val)
    my_heap.print_heap()


def _exercises():
    print("\n---------- find_kth_smallest exercise ----------")
    # Test cases
    nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
    ks = [2, 3, 4, 7]
    expected_outputs = [2, 3, 4, 5]

    for i in range(len(nums)):
        print(f'Test case {i + 1}...')
        print(f'Input: {nums[i]} with k = {ks[i]}')
        result = find_kth_smallest(nums[i], ks[i])
        print(f'Output: {result}')
        print(f'Expected output: {expected_outputs[i]}')
        print(f'Test passed: {result == expected_outputs[i]}')
        print('---------------------------------------')


    print("\n---------- stream_max exercise ----------")
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
        ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = stream_max(nums)
        print(f'\nTest {i + 1}')
        print(f'Input: {nums}')
        print(f'Expected Output: {expected}')
        print(f'Actual Output: {result}')
        if result == expected:
            print('Status: Passed')
        else:
            print('Status: Failed')



if __name__ == "__main__":
    _main()
    _exercises()
