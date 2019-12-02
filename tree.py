class Node:
    left = None
    right = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None:
        return Node(key, val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)
    return node

def search(node, key):
    if node.key == None:
        raise KeyError
    if node.key == key:
        return node.val
    elif key < node.key:
        return search(node.left, key)
    else: 
        return search(node.right, key)

class Tree:

    root = None

    def __init__(self, data):
        self.data = data

    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)

    def __getitem__(self, key):
        return search(self.root, key)

    def partition(self, data):
        left, right = [], []
        for i in range(len(self.data[0])-1):
            for row in data:
                if row[i] < row[len(row)//2]:
                    left.append(row)
                else:
                    right.append(row)
        return left, right

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node, depth=1):
        if node is None:
            return
        print(depth * " ", f"{node.val}")
        self._print_tree(node.left, depth+1)
        self._print_tree(node.right, depth+1)
    
t = Tree()
t[0] = "a"
t[1] = "b"
t[2] = "c"
t.print_tree()