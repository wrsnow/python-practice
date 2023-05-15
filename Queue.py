import random


class Queue:
    '''
    DASDASDASSDASDASD
    '''
    items = None
    start = None
    end = None
    max = None

    def __init__(self):
        self.items = []
        self.start = 0
        self.end = 0
        self.max = 10;

    def enqueue(self, element):
      if len(self.items) < self.max:
        self.items.append(element)
        self.end += 1
        return "Added to queue"
      else:
        return "Queue is full"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            self.items.pop(0)
            return "Item poped"

    def is_empty(self):
        return len(self.items) <= 0

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return -1

    def __repr__(self) -> str:
        return f'''
			items: {self.items}
			start: {self.start}
			end: {self.end}
			'''


queue = Queue()
for i in range(0, 14):
    print(queue.enqueue(random.randint(0, 100)))

for i in range(0, 10):
    print(queue)
    print(queue.dequeue())

print(queue.peek())