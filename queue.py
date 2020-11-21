class Node:
    def __init__(self, data, priority=2):
        self.data = data
        self.next = None
        self.previous = None
        self.priority = priority


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def empty(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def enqueue(self, obj):
        node = Node(obj)
        if self.last == None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def dequeue(self):
        if self.first == None:
            return
        if self.size == 1:
            self.first = None
            self._last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def get_first(self):
        print(str(self.first.data))


class PriorityQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.priority_size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def empty(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def enqueue(self, obj, priority=2):
        if priority != 2:
            self.priority_size += 1
            node = Node(obj, 1)
        else:
            node = Node(obj)
        if self.size == 0:
            self.first = node
            self.first.previous = None
            self.last = node
            self.last.next = None
            self.size += 1
            return
        temp = self.last
        self.last.next = node
        self.last = node
        self.last.previous = temp
        self.last.next = None
        self.size += 1

    def dequeue(self):
        if self.first == None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        if self.priority_size == 0:
            self.first = self.first.next
            self.first.previous = None
            tmp.next = None
            self.size -= 1
        else:
            while tmp.priority != 1:
                tmp = tmp.next
            tmp.previous.next = tmp.next
            tmp = None
            self.size -= 1
            self.priority_size -= 1

    def get_first(self):
        if self.priority_size == 0:
            return self.first.data
        tmp = self.first
        while tmp.priority != 1:
            tmp = tmp.next
        return tmp.data


class ArrayQueue:
    def __init__(self):
        self.queue = [None, None, None, None, None, None]
        self.first = 0
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def empty(self):
        self.first = 0
        self.size = 0

    def enqueue(self, obj):
        if self.size == len(self.queue):
            return "The queue is full. Please try later!"
        self.queue[(self.first + self.size) % len(self.queue)] = obj
        self.size += 1

    def dequeue(self, obj):
        if self.size == 0:
            return "The queue is empty."
        self.first = (self.first + 1) % len(self.queue)
        self.size -= 1



