class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

        
node = Node(10)
node.left = Node(5)
node.right = Node(10)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

# print(node.right.data)
# print(node.right.right.data)

myTree = Tree(node, 'Olga')
print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.right.data)




















