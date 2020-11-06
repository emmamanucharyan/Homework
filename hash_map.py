class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, index=None):
        self.capacity = 12
        self.hashtable = [None] * self.capacity
        self.size = 0
        self.index = index

    def _hash(self, element):
        # return hash(element) % self._capacity
        return ord(element[0]) % self.capacity

    def resize(self):
        n = 0
        while n != self.capacity:
            self.hashtable.append(None)
            n += 1
        self.capacity = self.capacity * 2


    def put(self, key, value):
        self.index = self._hash(key)
        # print(self.index)
        if self.size >= self.capacity/3:
            HashMap.resize(self)
        for i in range(self.index, len(self.hashtable)):
            if (self.hashtable[i] != None):
                if key == self.hashtable[i].key:
                    oldValue = self.hashtable[i].value
                    self.hashtable[i].value = value
                    return oldValue
            else:
                self.hashtable[self.index] = Entry(key, value)
                self.size += 1
                return None


    def remove(self, key):
        for i in range(len(self.hashtable)):
            if self.hashtable[i] != None:
                if key == self.hashtable[i].key:
                    self.hashtable[i] = None
                    return
        print("Nothing to remove at that key")

        pass

    def get(self, key):
        self.index = self._hash(key)
        for i in range(self.index, len(self.hashtable)):
            if (self.hashtable[i] != None):
                if key == self.hashtable[i].key:
                    return self.hashtable[i].value
            else:
                return None

    def has_key(self, key):
        for i in range(len(self.hashtable)):
            if self.hashtable[i] != None:
                print(self.hashtable[i].key)
                if key == self.hashtable[i].key:
                    return True
        return False

    def has_value(self, value):
        j = 0
        for i in range(len(self.hashtable)):
            if self.hashtable[i] != None:
                if value == self.hashtable[i].value:
                    j += 1
        if j == 0:
            return False
        else:
            print("There are", j, "elements with this value")
            return True

    def size(self):
        return self.size

    def print(self):
        print("printing hashset elements")
        for e in self.hashtable:
            # pass
            if e == None:
                print(None)
            else:
                print(e.value)
            # while (e != None):
            #     print(e.value)
            #     e = e.next

    def __iter__(self):
        for i in range(len(self.hashtable)):
            if (self.hashtable[i] != None):
                self.index = i
                break
        return self

    def __next__(self):
        if self.index >= len(self.hashtable):
            raise StopIteration
        tmp_index = self.index
        self.index = len(self.hashtable)
        for i in range(tmp_index + 1, len(self.hashtable)):
            if (self.hashtable[i] != None):
                self.index = i
                break
        return self.hashtable[tmp_index].value

    def return_hashtable(self):
        print(self.hashtable)


HM = HashMap()
# print(HM.put("a", "arbitrary"))
# # print(HM.put("a", "anything"))
# print(HM.put("e", "Aaron"))
# # print(HM.put("ac", "actor"))
# print(HM.put("b", "barbeque"))
HM.put("b", "doll")
HM.put("a", "dpp")
HM.put("c", "ccp")
# print(HM.put("g", "ggg"))
HM.put("e", "1")
HM.put("+", "2pddp")
print(HM.put("&", "3ssr"))
HM.put("?", "4ee")
HM.put("q", "5pddp")
HM.put("w", "6ssr")
HM.put("r", "7ee")
HM.put("t", "8pddp")
HM.put("y", "9ssr")
HM.put("u", "10ee")
# HM.put("i", "11ddp")
# HM.put("o", "12sr")
# HM.put("p", "13e")
# HM.put("s", "14ddp")
# HM.put("f", "15sr")
# HM.put("k", "16e")
# HM.put("h", "17ddp")
# HM.put("j", "18sr")
# HM.put("l", "19e")
# HM.put("!", "20ddp")
# HM.put("z", "21sr")
# HM.put("x", "22e")
# HM.put("v", "23ddp")
# HM.put("n", "24sr")
HM.put("$", "25e")
# HM.put("!", "26ddp")
# HM.put("@", "27sr")
# HM.put("#", "28e")
# HM.put("%", "29ddp")
# HM.put("^", "30sr")
# HM.remove("h")

# HM.remove("a")
for elem in HM:
    print(elem)
# HM.print()
#
HM.has_value("doll")
print(HM.has_key("a"))
# HM.print()
