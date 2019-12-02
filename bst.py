class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = Node(node)
        else:
            self.__insert_node(self.root, node)

    def __insert_node(self, root, node):
        if node < root.key:
            if root.left == None:
                root.left = Node(node)
            else:
                self.__insert_node(root.left, node)
        else:
            if root.right == None:
                root.right = Node(node)
            else:
                self.__insert_node(root.right, node)

    def size(self):
        return self.__rsize(self.root)

    def __rsize(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.__rsize(node.left) + self.__rsize(node.right)

    def in_order(self):
        self.__in_order_traverse(self.root)
    
    def __in_order_traverse(self, node):
        if node != None:
            self.__in_order_traverse(node.left)
            print(str(node.key))
            self.__in_order_traverse(node.right)

def partition(arr):
    piv = arr[0]
    arr = arr[1:]
    low = [x for x in arr if x <= piv]   
    hi = [x for x in arr if x >= piv]
    return low, piv, hi

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    low, piv, hi = partition(arr)
    return quick_sort(low) + [piv] + quick_sort(hi)

def gini_index(node, classes):
    gini = 0
    nstances = sum([len(group) for group in node])
    for group in node:
        size = len(group)
        score = 0
        for val in classes:
            p = [row[-1] for row in group].count(val) / size
            score += p**2
        gini += (1 - score) * (size / nstances)
    return gini


"""tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(2)

tree.in_order()
print("\n")
print(tree.size())
print("\n")
x = quick_sort([8, 2, 4, 9, 6, 1, 7, 5, 3])
print(x)"""