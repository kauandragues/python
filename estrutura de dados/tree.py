class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def retornar_node(self):
        return str(self.data)

class Tree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.simetric_traversal(node.left)

        if node.right:
            self.simetric_traversal(node.right)

    def possib(self, node=None)
        if node is None:
            node = self.root

        if word
            

if __name__ == "__main__":
    tree = Tree(Node())
    start = Node()
    e = Node("E")
    i = Node("I")
    s = Node("S")
    u = Node("U")
    a = Node("A")
    r = Node("R")
    w = Node("W")
    t = Node("T")
    n = Node("N")
    d = Node("D")
    k = Node("K")
    m = Node("M")
    g = Node("G")
    o = Node("O")

    tree.root.left = e
    tree.root.right = t 
    e.left = i 
    e.right = a 
    i.left = s
    i.right = u 
    a.left = r 
    a.right = w 
    t.left = n 
    t.right = m 
    n.left = d 
    n.right = k 
    m.left = g 
    m.right = o

    tree.simetric_traversal()