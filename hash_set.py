class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet:
    def __init__(self, capacity):
        self.hashtable = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def levelOrderIterator(self):
        for i in range(self.size):
            isYield = False
            for e in self.hashtable:
                for j in range(i):
                    if (e != None):
                        e = e.next
                if (e != None):
                    yield e.data
                    isYield = True
            if (isYield == False):
                break

    def _hash(self, element):
        # return hash(element) % self._capacity
        return ord(element[0]) % self.capacity

    def add(self, element):
        index = self._hash(element)
        print(type(index))
        print(index)
        if HashSet.contains(self, element):
            print("Object already in set")
            return
        if self.hashtable[index] == None:
            self.hashtable[index] = Node(element)
        else:
            n = Node(element, self.hashtable[index])
            self.hashtable[index] = n
            self.size += 1

    #     #TODO add only unique values to the set - DONE

    def contains(self, element):
        index = self._hash(element)
        n = self.hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        if not HashSet.contains(self, element):
            print("Not in set")
            return
        index = self._hash(element)
        n = self.hashtable[index]
        p = None
        while n != None:
            if n.data == element:
                if p == None:
                    self.hashtable[index] = n.next
                else:
                    p.next = n.next
                    n.next = None
                    self.size -= 1
                    return n
            p = n
            n = n.next
        return None

    def size(self):
        return self.size

    def intersection(self, s):
        newSet = HashSet(100)
        for e in self.hashtable:
            while (e != None):
                if (s.contains(e.data)):
                    newSet.add(e.data)
                e = e.next
        return newSet

    def intersection_update(self, s):
        for e in self.hashtable:
            while (e != None):
                if not s.contains(e.data):
                    r = e
                    e = e.next
                    self.remove(r.data)
                    continue
                else:
                    e = e.next
                 
    def union(self, s):
        newSet = HashSet(100)
        for e in s.hashtable:
            while (e != None):
                newSet.add(e.data)
                e = e.next
        for e in self.hashtable:
            while (e != None):
                if not s.contains(e.data):
                    newSet.add(e.data)
                e = e.next
        return newSet

    def union_update(self, s):
        for e in s.hashtable:
            while (e != None):
                if not self.contains(e.data):
                    self.add(e.data)
                e = e.next

    def subtraction(self, s):
        for e in s.hashtable:
            while (e != None):
                if self.contains(e.data):
                    self.remove(e.data)
                e = e.next                
                    

    def print(self):
        print("printing hashset elements")
        for e in self.hashtable:
            while (e != None):
                print(e.data)
                e = e.next

    def __iter__(self):

        for e in self.hashtable:
            if (e != None):
                self._elem = e
                break
        return self

    def __next__(self):
        if self._elem == None:
            raise StopIteration
        tmp = self._elem
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
        for i in range(index + 1, len(self.hashtable)):
            if (self.hashtable[i] != None):
                self._elem = self.hashtable[i]
                break
        return tmp.data

    # Generator example
    def evensUpTo(n):
        i = 0
        while(True):
            if (i >= n):
                break
            yield i
            i = i+2
    #
    # for e in evensUpTo(10):
    # print(e)


hhh = ["h"]
HS = HashSet(100)
HS.add("a")
HS.add("a")
HS.add("b")
HS.add("c")
HS.add("aa")
HS.add("ac")
HS.add("bb")
HS.add("D")
for elem in HS.levelOrderIterator():
    print(elem)
# ''''
HS1 = HashSet(100)
HS1.add("a")
HS1.add("b")
HS1.add(hhh)
# HS1.add(3)
# print()
# HS3 = HS.intersection(HS1)
# #print(HS3.size())
# #HS3.print()
HS.intersection_update(HS1)
# HS.print()
for elem in HS:
    print(elem)
