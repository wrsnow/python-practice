class Stack:
  data = []
  def __init__(self)->None:
    self.data = []

  def push(self,new_data)->str:
    self.data.append(new_data)
    return "Item inserted"

  def pop(self)->str:
    if self.is_empty():
      return "The stack is empty"
    popped = self.data.pop()
    return f"{popped} was removed"

  def is_empty(self):
    return len(self.data) <= 0

  def peek(self)->str:
    if self.is_empty():
      return "The stack is empty"
    return self.data[-1]

  def clear(self)->None:
    while len(self.data) > 0:
      self.data.pop()

  def search(self,element):
    try:
      return self.data.index(element)
    except ValueError:
      return -1

  def __repr__(self) -> str:
			return f"{self.data}"

stack = Stack()

for i in range(50):
  stack.push(i)


print(stack)
stack.push(4)
print(stack.search(4))
stack.clear()
print(f"Stack: {stack}")
