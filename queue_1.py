import random


class CircularBufferList:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def put(self, item):
        self.buffer[self.head] = item
        if self.count == self.size:
            self.tail = (self.tail + 1) % self.size
        else:
            self.count += 1
        self.head = (self.head + 1) % self.size

    def get(self):
        if self.count == 0:
            raise IndexError("Empty queue!")
        item = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.size
        self.count -= 1
        return item

    def __str__(self):
        return " ".join(
            map(
                str,
                [self.buffer[(self.tail + i) % self.size] for i in range(self.count)]
            )
        )


# Test
queue = CircularBufferList(5)
for _ in range(queue.size):
    put_value = random.randint(-100, 100)
    queue.put(put_value)
    print(f"put({put_value}) Queue: {queue}")

print(f"get({queue.get()}) Queue: {queue}")

for _ in range(3):
    put_value = random.randint(-100, 100)
    queue.put(put_value)
    print(f"put({put_value}) Queue: {queue}")
