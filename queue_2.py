from collections import deque
import random

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)
        self.size = size

    def put(self, item):
        self.buffer.append(item)

    def get(self):
        return self.buffer.popleft()

    def __str__(self):
        return str(self.buffer)

# Test
queue = CircularBufferDeque(5)
for _ in range(queue.size):
    put_value = random.randint(-100, 100)
    queue.put(put_value)
    print(f"put({put_value}) Queue: {queue}")

print(f"get({queue.get()}) Queue: {queue}")

for _ in range(3):
    put_value = random.randint(-100, 100)
    queue.put(put_value)
    print(f"put({put_value}) Queue: {queue}")