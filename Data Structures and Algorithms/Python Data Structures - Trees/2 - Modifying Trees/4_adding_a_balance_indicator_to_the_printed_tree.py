#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Fri Oct 7 08:38:12 2022

@author: Januario Cipriano
"""

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
        
    
    def add(self, data):
        if self.data == data:
            return 
        
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
                
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
    
    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data
                
    def delete(self, target):
        if self.data == target:
            if self.left and self.right:
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)
                return self
            else:
                return self.left or self.right
        
        if self.right and target > self.data:
            self.right = self.right.delete(target)
        if self.left and target < self.data:
            self.left = self.left.delete(target)
        return self
    
        
    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            # nodes.append(self.data)
            nodes.append(self)
            return nodes
        
        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
            
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes
        
        
    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)
    
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
        
    def isBalanced(self):
        leftHeight = self.left.height()+1 if self.left else 0
        rightHeight = self.right.height()+1 if self.right else 0
        return abs(leftHeight - rightHeight) < 2
    
    def toStr(self):
        if not self.isBalanced():
            return str(self.data)+'*'
        return str(self.data)
        

        
class Tree:
    def __init__(self, root, name='--Tree Name Here--'):
        self.root = root
        self.name = name
        
    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        # spacing = spacing-len(str(n))+1
        # return str(n)+(' '*spacing)
        spacing = spacing-len(n.toStr())+1
        return n.toStr()+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')
        
    def search(self, target):
        return self.root.search(target)
        
    def traversePreorder(self):
        self.root.traversePreorder()
        
    def traverseInorder(self):
        self.root.traverseInorder()
        
    def traversePostorder(self):
        self.root.traversePostorder()
        
    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)
        
    def height(self):
        return self.root.height()
    
    def add(self, data):
        self.root.add(data)
        
    def delete(self, target):
        self.root = self.root.delete(target)
        
    def isBalanced(self):
        return self.root.isBalanced()
    
    # def toStr(self):
    #     return self.root.toStr()



tree = Tree(Node(50), 'An Unbalanced Tree')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.right.right = Node(100)
tree.root.right.right.right = Node(150)

tree.print()


















