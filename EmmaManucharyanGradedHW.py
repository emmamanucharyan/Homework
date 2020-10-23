############      No.1      ###############

class Dequeue:

    def __init__(self):
        self.queue = [None, None, None, None]
        self.size = 0
        self.front = -1
        self.rear = -1

    def resize(self):
        initial_length = len(self.queue)
        temp = []
        j = 0
        for i in self.queue:
            while j < len(self.queue):
                temp.append(self.queue[self.front])
                self.front = (self.front + 1) % initial_length
                j += 1
        j = 0
        while j < initial_length:
            temp.append(None)
            self.queue = temp
            print(self.queue)
            j += 1
        self.front = 0
        self.rear = self.queue[initial_length - 1]

    def insert_front(self, obj):
        if self.size == len(self.queue):
            que.resize()
        if self.size == 0:
            self.front = (self.front + 1) % len(self.queue)
            self.rear = (self.front + 1) % len(self.queue)
            self.queue[self.front] = obj
            self.size += 1
            return
        self.front = (self.front - 1) % len(self.queue)
        self.queue[self.front] = obj
        self.size += 1

    def remove_front(self):
        if self.size == 0:
            print("Empty")
            return
        if self.size == 1:
            self.front = self.rear
            self.queue[self.front] = None
            self.size -= 1
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)

    def remove_end(self):
        if self.size == 0:
            print("Empty")
            return
        if self.size == 1:
            self.front = self.rear
            self.queue[self.rear] = None
            self.size -= 1
            return
        self.queue[self.rear] = None
        self.rear = (self.rear - 1) % len(self.queue)

    def insert_end(self, obj):
        if self.size == len(self.queue):
            que.resize()
        if self.size == 0:
            self.front = (self.front + 1) % len(self.queue)
            self.rear = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = obj
            return
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = obj

    def get_first(self):
        if self.size == 0:
            print("Empty")
            return
        return self.queue[self.front]

    def get_last(self):
        if self.size == 0:
            print("Empty")
            return
        return self.queue[self.rear]

    def display_queue(self):
        i = self.front
        while i != self.rear:
            print(self.queue[i])
            i = (i + 1) % len(self.queue)

    def print_current_queue(self):
        print(self.queue)

que = Dequeue()


############      No. 3      ###############

class Node:
    def __init__(self, data, next=None, previous=None, position=0):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def size(self):
        return self.size

    def first(self):
        return self.first

    def last(self):
        return self.last

    def print_list(self):
        print("Printing Linked List Elements")
        current = self.first
        while current is not None:
            print(str(current.data))
            current = current.next

    def insert_first(self, obj):
        if self.size == 0:
            node = Node(obj)
            self.first = node
            self.first.previous = None
            self.last = node
            self.last.next = None
            self.size += 1
            return
        node = Node(obj)
        self.size += 1
        node.next = self.first
        self.first.previous = node
        self.first = node
        self.first.previous = None

    def insert_last(self, obj):
        node = Node(obj, None)
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

    def insert_after(self, obj, new_obj):
        if self.size == 0:
            print("List is empty")
            return
        else:
            current = self.first
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                node = Node(new_obj)
                node.previous = current
                node.next = current.next
                if current.next is not None:
                    current.next.previous = node
                current.next = node

    def insert_before(self, obj, new_obj):
        if self.size == 0:
            print("List is empty")
            return
        else:
            current = self.first
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                node = Node(new_obj)
                node.next = current
                node.previous = current.previous
                if current.previous is not None:
                    current.previous.next = node
                current.previous = node

    def remove_before(self, obj):
        if self.size == 0:
            print("List is empty")
            return
        elif self.first.data == obj:
            print("No elements before this one")
        elif self.size == 2:
            self.first = None
            self.first = self.last
            self.size -= 1
        elif self.first.next.data == obj:
            temp = self.first
            self.first = None
            self.first = temp.next
        else:
            current = self.first.next.next
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                current.previous = current.previous.previous
                current.previous.next = current

    def index_of(self, obj):
        if self.size == 0:
            print("List is empty")
            return
        position = 1
        current = self.first
        while current != None:
            if current.data == obj:
                print("index is", position)
                return position
            position += 1
            current = current.next
        print("Item not found in list")

    def remove_by_value(self, obj):
        if self.size == 0:
            print("The list has no element to delete")
            return
        if self.first.next is None:
            if self.first.data == obj:
                self.first = None
                self.last = None
                self.size -= 1
            else:
                print("Item not found")
            return

        if self.first.data == obj:
            self.first = self.first.next
            self.first.previous = None
            self.size -= 1
            return

        current = self.first
        while current.next is not None:
            if current.data == obj:
                break
            current = current.next
        if current.next is not None:
            current.previous.next = current.next
            current.next.previous = current.previous
            self.size -= 1
        else:
            if current.data == obj:
                self.last = self.last.previous
                self.size -= 1
            else:
                print("Element not found")

    def reverse_list(self):
        if self.size == 0:
            print("The list has no elements to reverse")
            return
        if self.size == 1:
            return
        current = self.first
        after_current = current.next
        current.next = None
        current.previous = after_current
        while after_current is not None:
            after_current.previous = after_current.next
            after_current.next = current
            current = after_current
            after_current = after_current.previous
        self.first = current

    def remove_numeric_nodes(self):
        if self.size == 0:
            print("The list has no element to delete")
            return
        if self.first.next is None:
            if self.first.data.isnumeric() == True:
                self.first = None
                self.size -= 1
            else:
                print("No numeric node")
                return

        if str(self.first.data).isnumeric() == True:
            self.first = self.first.next
            self.first.previous = None
            self.size -= 1

        current = self.first
        while current.next is not None:
            if str(current.data).isnumeric() == True:
                current.previous.next = current.next
                current.next.previous = current.previous
                self.size -= 1
            current = current.next
        if current.next is None:
            if str(current.data).isnumeric() == True:
                current.previous.next = None
                self.size -= 1
            else:
                print("No numeric nodes")

    def remove_nodes_at_even_position(self):
        if (self.size % 2) == 0:
            self.last = self.last.previous
            self.last.next = None
        print(type(self.last.previous))
        current = self.first.next
        while current is not None:
            dllist.remove_by_value(current.data)
            if current.next is not None:
                current = current.next.next
            else:
                break

    def test_first(self, obj):
        if self.first.data == obj:
            return True
        else:
            return False

    def test_last(self, obj):
        if self.last.data == obj:
            return True
        else:
            return False

    ############    No. 4 with test   ###############

    def split_even_odd_into_new_lists(self):
        even_dllist = DoubleLinkedList()
        odd_dllist = DoubleLinkedList()
        if self.size == 0:
            print("list is empty")
            return
        if self.size == 1:
            odd_dllist.insert_last(self.first.data)
            odd_dllist.print_list()
            print("No even position elements")
            return
        current = self.first
        if self.size == 2:
            odd_dllist.insert_last(self.first.data)
            even_dllist.insert_last(self.last.data)
            odd_dllist.print_list()
            even_dllist.print_list()
            return
        if self.size == 3:
            odd_dllist.insert_last(self.first.data)
            even_dllist.insert_last(self.first.next.data)
            odd_dllist.insert_last(self.last.data)
            odd_dllist.print_list()
            even_dllist.print_list()
            return

        while current.next.next is not None:
            odd_dllist.insert_last(current.data)
            even_dllist.insert_last(current.next.data)
            current = current.next.next
        if (self.size % 2) == 0:
            odd_dllist.insert_last(self.last.previous.data)
            even_dllist.insert_last(self.last.data)
        else:
            odd_dllist.insert_last(self.last.data)
        odd_dllist.print_list()
        even_dllist.print_list()


dllist = DoubleLinkedList()

dllist.insert_first(3)
dllist.insert_first(2)
dllist.insert_first(1)
dllist.insert_last(4)
dllist.insert_last(5)
dllist.insert_last(6)
dllist.print_list()
dllist.split_even_odd_into_new_lists()
print(dllist.first)

############      No. 2      ###############






#############      No. 5         ##############


