from c_library_cython.queue import Queue

q = Queue()

q.append(5)
print(q.peek())
print(q.pop())
