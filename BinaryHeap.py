import numpy as np
from Interfaces import Queue



def left(i : int):
    # todo
    return 2 * i + 1

def right(i: int):
    # todo
    return 2 * (i+1)

def parent(i : int):
    # todo
    return (i-1) // 2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        # todo
        b = self.new_array(max(2*self.n , 1))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def add(self, x : object):
        # todo
        if len(self.a) < self.n + 1:
            self.resize()
        self.a[self.n] = x
        self.n = self.n + 1
        self.bubble_up(self.n - 1)
        return True

    def bubble_up(self, i):
        # todo
        if i < 0 or i >= self.n:
            raise IndexError("Can't do that.") # Raise Exception error!!!!
        self.p = parent(i)
        while i > 0 and self.a[i] < self.a[self.p]:
            self.a[i] , self.a[self.p] = self.a[self.p] , self.a[i]
            i = self.p
            self.p = parent(i)

    def remove(self):
        # todo
        if self.n == 0:
            raise IndexError("Can't do that.") # raise Exception Here!!!!
        self.x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n = self.n - 1
        self.trickle_down(0)
        if 3 * self.n < len(self.a):
            self.resize()
        return self.x

    def trickle_down(self, i):
        # todo
        while i >= 0:
            self.j = -1
            self.r = right(i)
            if self.r < self.n and self.a[self.r] < self.a[i]:
                self.l = left(i)
                if self.a[self.l] < self.a[self.r]:
                    self.j = self.l
                else:
                    self.j = self.r
            else:
                self.l = left(i)
                if self.l < self.n and self.a[self.l] < self.a[i]:
                    self.j = self.l
            if self.j >= 0:
                self.a[self.j] , self.a[i] = self.a[i] , self.a[self.j]
            i = self.j

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

x = BinaryHeap()
x.add(2)
x.add(1)
x.add(5)
print(x.size())
print(x.remove())
x.add(4)
x.add(1)
x.add(3)
print(x.size())
print(x.remove())
print(x.remove())
print(x.remove())
print(x.remove())
print(x.remove())
