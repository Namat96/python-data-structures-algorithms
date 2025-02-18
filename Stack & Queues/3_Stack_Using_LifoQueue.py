from queue import LifoQueue
stack = LifoQueue(maxsize=5)
stack.put(10)
stack.put(20)
stack.put(30)
print("Stack Size = ", stack.qsize())
print("Stack poped = ", stack.get())
print("Stack Size = ", stack.qsize())
