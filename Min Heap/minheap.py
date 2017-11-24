"""
MIN HEAP IMPLEMENTATION by Ali Momin
Date: 23/11/2017
"""

class MaxHeap:
    def __init__(self):
        self.array = []

    def getleft(self, index):
        if 2*index >= len(self.array):
            return False
        return self.array[2*index]

    def getright(self, index):
        if 2*index + 1 >= len(self.array):
            return False
        return self.array[2*index + 1]

    def getparent(self, index):
        if index is 0: return False
        if index%2 is 0:
            return index/2
        else:
            return (index - 1)/2

    def heapify(self, index):
        parent = self.getparent(index)
        if parent is False or parent is 0:
            return True
        while self.array[parent] < self.array[index]:
            temp = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = temp
            index = parent
            parent = self.getparent(parent)
            if parent is False or parent is 0:
                break
        return True

    def insert(self, value):
        if len(self.array) is 0:
            self.array.append(None)
        self.array.append(value)
        self.heapify(len(self.array) - 1)

    def pop(self):
        if len(self.array) is 1 or len(self.array) is 0:
            return False
        ret = self.array.pop(1)
        for x in range(0, len(self.array)):
            self.heapify(x)
        return ret

    def __str__(self):
        return self.array.__str__()


""" ---------------------------- BELOW is just for testing the Min Heap Implementation ---------------------------- """

# max = MaxHeap()
#
# max.insert(4)
# max.insert(3)
# max.insert(2)
# max.insert(2)
# max.insert(1)
# max.insert(2)
# max.insert(1)
# max.insert(1)
#
# print max
#
# max.insert(5)
# max.insert(10)
# max.insert(8)
#
# print max
#
# print max.pop()
#
# print max

""" ------------------------- EXAMPLE usage of Min Heap for Heap Sort in Descending Order ------------------------- """

unsorted = []

unsorted.append(5)
unsorted.append(7)
unsorted.append(10)
unsorted.append(20)
unsorted.append(15)
unsorted.append(2)

print unsorted

sorted = []

max = MaxHeap()

for x in unsorted:
    max.insert(x)

t = max.pop()
while t is not False:
    sorted.append(t)
    t = max.pop()

print sorted

