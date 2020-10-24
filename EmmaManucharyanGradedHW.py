############      No.1      ###############

class Dequeue:

    def __init__(self):
        self.queue = [None, None]
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
            j += 1
        print("Resize:", self.queue, "\n")
        self.front = 0
        self.rear = initial_length-1



    def insert_front(self, obj):
        if self.size == len(self.queue):
            que.resize()
        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.queue[self.front] = obj
            self.size = 1
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
        self.size -= 1


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
        self.size -= 1




    def insert_end(self, obj):
        if self.size == len(self.queue):
            que.resize()
        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = obj
            self.size = 1
            return
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = obj
        self.size += 1


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
        print("List is ")
        while i != self.rear:
            print(self.queue[i])
            i = (i + 1) % len(self.queue)
        print(self.queue[self.rear])
        print()


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
        print()

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
                self.last.next = None
                self.size -= 1
            else:
                print("Element not found")

    def reverse_list(self):
        if self.size == 0:
            print("The list has no elements to reverse")
            return
        if self.size == 1:
            return
        temp = self.first
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
        self.last = temp

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

    ############    No. 4  with test  ###############

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



############      No. 2      ###############


class DeQueue(DoubleLinkedList):

    def __init__(self):
        super().__init__()
        self.first = None
        self.last = None
        self.size = 0


    def display(self):
        self.print_list()

    def print(self):
        h = self.last.data
        self.remove_by_value(1)

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue_front(self, obj):
        self.insert_first(obj)

    def enqueue_back(self, obj):
        self.insert_last(obj)

    def get_back(self):
        if self.is_empty():
            return None
        print(self.last.data)
        return self.last.data

    def get_front(self):
        if self.is_empty():
            return None
        print(self.first.data)
        return self.first.data

    def dequeue_front(self):
        if self.is_empty():
            print("Empty")
            return
        self.remove_by_value(self.first.data)

    def dequeue_back(self):
        if self.is_empty():
            print("Empty")
            return
        self.remove_by_value(self.last.data)


dque = DeQueue()


#############      No. 5         ##############

def main():
    def test_array_dequeue():
        global que
        print("TESTING 1, ARRAY_DEQUEUE \n")
        que.insert_front(1)
        print("First is:", que.get_first())
        if que.get_first() == 1:
            print("True")
        que.display_queue()
        que.insert_end(2)
        print("Last is:", que.get_last())
        if que.get_last() == 2:
            print("True")
        que.display_queue()
        que.insert_end(3)
        que.display_queue()
        que.remove_front()
        que.display_queue()
        print("First is:", que.get_first())
        if que.get_first() == 2:
            print("True")


    def test_double_linked_list():
        global dllist
        print("TESTING 3, Double Linked List \n")
        dllist.insert_first("w")
        dllist.insert_last(5)
        dllist.insert_first("a")
        dllist.insert_first(2)
        dllist.insert_last("b")
        dllist.insert_first(0)
        print("List is: 0<=>2<=>a<=>w<=>5<=>b", "\t Let's Check")
        dllist.print_list()
        print(dllist.test_first(0))
        print(dllist.test_last("b"))
        dllist.remove_by_value("w")
        dllist.remove_by_value("b")
        dllist.insert_before(5, 4)
        dllist.print_list()
        print("Reversed List:")
        dllist.reverse_list()
        dllist.print_list()
        print(dllist.test_first(5))
        print(dllist.test_last(0))

    def test_split_list():
        print("TESTING 4, Double Llist Split \n")
        dlist = DoubleLinkedList()
        dlist.insert_first(3)
        dlist.insert_first(2)
        dlist.insert_first(1)
        dlist.insert_last(4)
        dlist.insert_last(5)
        dlist.insert_last(6)
        dlist.print_list()
        dlist.split_even_odd_into_new_lists()
        print(dllist.first)


    def test_dllist_dequeue():
        global dque
        print("TESTING 2, Double Llist_DEQUEUE \n")
        dque.insert_first(3)
        dque.insert_first(2)
        dque.insert_first(1)
        dque.insert_last(4)
        dque.insert_last(5)
        dque.insert_last(6)
        dque.print_list()

        dque.enqueue_front(8)

        dque.dequeue_back()
        dque.print_list()
        print("Front is:")
        dque.get_front()
        print("End is:")
        dque.get_back()

    test_array_dequeue()
    test_double_linked_list()
    test_split_list()
    test_dllist_dequeue()

main()
