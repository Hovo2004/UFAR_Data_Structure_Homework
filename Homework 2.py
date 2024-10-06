# Homework 1
def insertion_sort_recursive(arr, i=1):
    if i == len(arr):
        return

    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

    insertion_sort_recursive(arr, i + 1)


arr = [12, 11, 13, 5, 6]
insertion_sort_recursive(arr)
# print("Sorted array is:", arr)


# Homework 2

class CustomQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q = CustomQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element (peek):", q.peek())

print("Dequeue element:", q.dequeue())
print("Dequeue element:", q.dequeue())

print("Is queue empty?", q.is_empty())

q.enqueue(40)

print("Queue size:", q.size())

print("Dequeue element:", q.dequeue())
print("Dequeue element:", q.dequeue())

print("Dequeue element:", q.dequeue())
