import random


class Queue:
    items = None
    start = None
    end = None

    def __init__(self):
        self.items = []
        self.start = 0
        self.end = 0

    def enqueue(self, element) -> None:
        self.items.append(element)
        self.end += 1
        print("")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            tempArr = []
            for i in range(0, len(self.items)):
                if i == 0:
                    pass
                else:
                    tempArr.append(self.items[i])
            self.items = tempArr
            self.end -= 1
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
for i in range(0, 10):
    queue.enqueue(random.randint(0, 100))
for i in range(0, 10):
    print(queue.dequeue())
    print(queue.peek())
