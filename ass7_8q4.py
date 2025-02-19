
class Employee:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    
    def __add__(self, o):
        return Employee(self.n + " & " + o.n, self.s + o.s)
    
    def __sub__(self, o):
        return self.s - o.s

    def show(self):
        print(self.n, self.s)

e1 = Employee("a", 1000)
e2 = Employee("b", 1500)
e3 = e1 + e2
e3.show()
print(e1 - e2)