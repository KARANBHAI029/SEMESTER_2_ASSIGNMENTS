class Node:
    def __init__(self, d):
        self.d = d
        self.n = None

class LinkedList:
    def __init__(self):
        self.h = None

    def add(self, d):
        n = Node(d)
        if not self.h:
            self.h = n
        else:
            t = self.h
            while t.n:
                t = t.n
            t.n = n

    def remove(self, d):
        if not self.h:
            return
        if self.h.d == d:
            self.h = self.h.n
            return
        t = self.h
        while t.n and t.n.d != d:
            t = t.n
        if t.n:
            t.n = t.n.n

    def show(self):
        t = self.h
        while t:
            print(t.d, end=" -> ")
            t = t.n
        print("None")

l = LinkedList()
l.add(5)
l.add(10)
l.add(15)
l.show()
l.remove(10)
l.show()
