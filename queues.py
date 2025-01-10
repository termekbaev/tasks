from collections import deque
import random, time


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

class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)
        self.size = size

    def put(self, item):
        self.buffer.append(item)

    def get(self):
        return self.buffer.popleft()

    def __str__(self):
        return " ".join(
            map(
                str,
                self.buffer
            )
        )

def check_time(queue):
    start_time = time.time()
    for _ in range(10000):
        queue.put(random.randint(-100, 100))

    for _ in range(100):
        try:
            queue.get()
        except IndexError:
            pass

    for _ in range(1000):
        queue.put(random.randint(-100, 100))
    end_time = time.time()
    print(f'{queue.__class__.__name__} time: {end_time - start_time:.10f}')

# Test
queue_1 = CircularBufferList(500)
queue_2 = CircularBufferDeque(500)
check_time(queue_1)
check_time(queue_2)


