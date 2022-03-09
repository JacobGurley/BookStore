import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        #todo
        if u == self.nil:
            return -1
        self.d = 0
        while u != self.r:
            u = u.parent
            self.d = self.d + 1
        return self.d



    def size(self) -> int:
        return self._size(self.r)
    
    def _size(self, u : Node) -> int:
        # todo
        if u == self.nil:
            return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        # todo
        self.u = self.r
        prv = self.nil
        self.n = 0
        while self.u != self.nil:
            if prv == self.u.parent:
                self.n = self.n + 1
                if self.u.left != self.nil:
                    nxt = self.u.left
                elif self.u.right != self.nil:
                    nxt = self.u.right
                else:
                    nxt = self.u.parent
            elif prv == self.u.left:
                if self.u.right != self.nil:
                    nxt = self.u.right
                else:
                    nxt = self.u.parent
            else:
                nxt = self.u.parent
            prv = self.u
            self.u = nxt
        return self.n

    def height(self) -> int:
        return self._height(self.r)
    
    def _height(self, u : Node) -> int:
        # todo
        if u == self.nil:
            return 0
        return 1 + max(self._height(u.left),self._height(u.right))
    
    def traverse(self, u : Node):
        #todo
        if u == self.nil:
            self.traverse(u.left)#might have to remove from if
            self.traverse(u.right)#might have to remove from if

    def traverse2(self):
        # todo
        self.u = self.r
        prv = self.nil
        while self.u != self.nil:
            if prv == self.u.parent:
                if self.u.left != self.nil:
                    nxt = self.u.left
                elif self.u.right != self.nil:
                    nxt = self.u.right
                else:
                    nxt = self.u.parent
            elif prv == self.u.left:
                if self.u.right != self.nil:
                    nxt = self.u.right
                else:
                    nxt = self.u.parent
            else:
                nxt = self.u.parent
            prv = self.u
            self.u = nxt





    def bf_traverse(self):
        # todo
        q = ArrayQueue.ArrayQueue()
        l = list()
        if self.r != self.nil:
            q.add(self.r)
            l.append(self.r.v)
        while q.size() > 0:
            u = q.remove() #might need to add self.u
            if u.left != self.nil:
                q.add(u.left)
                l.append(u.left.v)
            if u.right != self.nil:
                q.add(u.right)
                l.append(u.right.v)
        return l

            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def in_order(self, u : Node, l : list) :       
        # todo

        if u.left != self.nil:
            self.in_order(u.left,l)
        l.append(u.v)
        if u.right != self.nil:
            self.in_order(u.right,l)
        return l


    def pre_order(self, u : Node, l : list):
        # todo
        l.append(u.v)
        if u.left != self.nil:
            self.pre_order(u.left, l)
        if u.right != self.nil:
            self.pre_order(u.right, l)
        return l

    def post_order(self, u : Node, l : list):
        # todo
        if u.left != self.nil:
            self.post_order(u.left, l)
        if u.right != self.nil:
            self.post_order(u.right, l)
        l.append(u.v)
        return l

    def __str__(self):
        l = []
        self.in_order(self.r, l)
        return ', '.join(map(str, l))
