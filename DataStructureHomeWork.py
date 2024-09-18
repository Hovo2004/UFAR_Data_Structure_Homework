class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0



# 1.1
l = []
for i in range(1, 6):
    l.append(i)

# 1.2
dictionary = {}
dictionary["one"] = 28
dictionary["two"] = 36
dictionary["three"] = 93
dictionary["four"] = 656
dictionary["five"] = 2355

# 1.3
st = Stack()
for i in range(1, 6):
    st.push(i)

# 1.4
que = Queue()
for i in range(1, 6):
    que.enqueue(i)

# 2.1
sum1 = 0
for i in range(len(l)):
    sum1 += l[i]

print(sum1)

# 2.2
sum2 = 0
for key in dictionary.keys():
    sum2 += dictionary[key]

print(sum2)

# 2.3
for i in range(1, 3):
    que.dequeue()

for item in que.items:
    print(item)

# 2.4
for i in range(1, 3):
    st.pop()

for item in st.items:
    print(item)
