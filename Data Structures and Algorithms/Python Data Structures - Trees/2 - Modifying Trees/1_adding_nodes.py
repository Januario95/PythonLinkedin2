#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Fri Oct 7 07:30:18 2022

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
    
        
    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
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
        

        
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
        
    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

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
        
    def add(self, data):
        self.root.add(data)
        
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



tree = Tree(Node(50)) #, 'Get all nodes at depth')
tree.root.left = Node(25)
tree.root.right = Node(75)

tree.print()
tree.add(10)
tree.add(76)
tree.add(75)
tree.print()
















