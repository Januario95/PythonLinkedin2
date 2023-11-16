class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def search(self, target):
        if self.data == target:
            print('Found it!')
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print('Value is not in tree')
    
    def traversePreorder(self):
        print(self.data, end=', ')
        if self.left:
            self.left.traversePreorder()
                
        if self.right:
            self.right.traversePreorder()
            
    def traverseInorder(self):
        if self.left:
            self.left.traversePreorder()
        print(self.data, end=', ')
        if self.right:
            self.right.traversePreorder()
        
    def traversePostorder(self):
        if self.left:
            self.left.traversePreorder()
            
        if self.right:
            self.right.traversePreorder()
        print(self.data)
        

        
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
        
    def search(self, target):
        return self.root.search(target)
        
    def traversePreorder(self):
        self.root.traversePreorder()
        
    def traverseInorder(self):
        self.root.traverseInorder()
        
    def traversePostorder(self):
        self.root.traversePostorder()


tree = Tree(Node(50), 'Tree Traversals')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)

print('Traverse Pre-Order')
tree.traversePreorder()

print('Traverse In-Order')
tree.traverseInorder()

print('Traverse Post-Oder')
tree.traversePostorder()













