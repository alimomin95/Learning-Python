class Node:
    def __init__(self):
        self.data = None
        self.nxt = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.iterator = None
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.head and not self.iterator:
            self.iterator = self.head
            return self.iterator
        elif self.iterator:
            self.iterator = self.iterator.nxt
            if self.iterator:
                return self.iterator
            raise StopIteration
        else:
            raise StopIteration

def __len__(self):
    count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.nxt
    return count

def append(self, data):
    if self.head is None:
        self.head = Node()
        self.tail = self.head
        if self.tail.data is not None:
            node = Node()
            node.data = data
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node
            return True
    else:
        self.tail.data = data
            return True

def pop(self, index):
    i = int(index)
    if i >= len(self):
        return False
        temp = self.head
        for x in range(i):
            temp = temp.nxt
    if temp is self.head:
        return self.popleft()
        if temp is self.tail:
            return self.popright()
    prev = temp.prev
        nxt = temp.nxt
        ret = temp.data
        prev.nxt = nxt
        nxt.prev = prev
        return ret

def popleft(self):
    if self.head is None:
        return None
        ret = self.head.data
        self.head = self.head.nxt
        return ret

    def popright(self):
        if self.tail is None:
            return None
        ret = self.tail.data
        if self.tail is self.head:
            self.head = None
            self.tail = None
            return ret
        temp = self.tail.prev
        temp.nxt = None
        self.tail = temp
        return ret

def __str__(self):
    l = []
    temp = self.head
        while temp is not None:
            l.append(temp.data)
            temp = temp.nxt
    return l.__str__()


""" --------------------------- BELOW is just for testing the Linked List Implementation --------------------------- """

# t1 = LinkedList()
#
# t1.append("foo")
# # t1.append("bar")
# # t1.append("bro")
#
# print len(t1)
#
# # for a in t1:
# #     print a.data,
#
# print t1.popright()
#
# t1.append("this")
# t1.append("is")
# t1.append("cool")
#
# print len(t1)
#
# print t1
#
# print t1.pop(1)
# print t1.pop(1)
# print t1.pop(0)
#
# print len(t1)
#
# t1.append(1)
# t1.append(2)
# t1.append(3)
#
# print t1

