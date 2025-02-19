class Queue:
    def __init__(self):
        self.q = []
    
    def enq(self, d):
        self.q.append(d)
    
    def deq(self):
        if self.q:
            return self.q.pop(0)
    
    def show(self):
        print(self.q)

q = Queue()
q.enq(1)
q.enq(2)
q.enq(3)
q.show()
q.deq()
q.show()
