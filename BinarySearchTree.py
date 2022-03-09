from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil

    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u

    def find_last(self, x: object) -> BinaryTree.Node:
        # todo
        self.w = self.r
        prev = self.nil
        while self.w != self.nil:
            prev = self.w
            if x < self.w.x:
                self.w = self.w.left
            elif x > self.w.x:
                self.w = self.w.right
            else:
                return self.w
        return prev

    def add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        # todo
        if p == self.nil:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n = self.n + 1
        return True

    def find_eq(self, x: object) -> object:
        # todo
        self.w = self.r
        while self.w != self.nil:
            if x < self.w.x:
                self.w = self.w.left
            elif x > self.w.x:
                self.w = self.w.right
            else:
                return self.w
        return self.nil

    def find(self, x: object) -> object:
        # todo
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        if z == self.nil:
            return self.nil
        return z.v

    def add(self, key: object, value: object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))

    def add_node(self, u: BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left != self.nil:
            self.s = u.left
        else:
            self.s = u.right
        if u == self.r:
            self.r = self.s
            self.p = self.nil
        else:
            self.p = u.parent
            if self.p == u:
                self.p.left = self.s
            else:
                self.p.right = self.s
        if self.s != self.nil:
            self.s.parent = self.p
        self.n = self.n - 1

    def remove_node(self, u: BinaryTree.Node):
        # todo
        if u == self.nil:
            return None
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            self.w = u.right
            while self.w.left != self.nil:
                self.w = self.w.left
            u.x = self.w.x
            u.v = self.w.v
            self.splice(self.w)

    def remove(self, x: object) -> bool:
        # todo
        self.p = self.find_eq(x)
        self.remove_node(self.p)
        if self.p != None:
            return True
        else:
            return False

    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


